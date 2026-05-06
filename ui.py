import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import threading
from encryption import encrypt, decrypt, generate_key
from network import Server, Client

class ChatApp:
    def __init__(self, root, role='server', net_kwargs=None):
        self.root = root
        self.role = role
        
        # 🔑 SHARED KEY - BOTH LAPTOPS MUST USE THE SAME KEY
        self.key = bytes.fromhex('0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef')
        # OR simpler: self.key = b'\x00' * 32
        
        self.running = True
        
        # Set default net_kwargs if not provided
        if net_kwargs is None:
            net_kwargs = {'host': 'localhost', 'port': 5000}

        # Initialize network
        try:
            if role == 'server':
                self.net = Server(host=net_kwargs['host'], port=net_kwargs['port'])
                # Wait for client in background
                threading.Thread(target=self._wait_server, daemon=True).start()
            else:
                self.net = Client(host=net_kwargs['host'], port=net_kwargs['port'])
                # Start receiving in background
                threading.Thread(target=self.receive_loop, daemon=True).start()
        except Exception as e:
            messagebox.showerror("Connection Error", f"Failed to connect: {e}")
            raise

        # Build UI
        self.build_ui()

    def build_ui(self):
        """Create Tkinter GUI"""
        # Chat display area
        self.chat_box = ScrolledText(self.root, state='disabled', height=20, width=70)
        self.chat_box.pack(padx=10, pady=10, fill='both', expand=True)

        # Input frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(padx=10, pady=5, fill='x')

        self.entry = tk.Entry(input_frame, width=60)
        self.entry.pack(side='left', padx=5)
        self.entry.bind('<Return>', lambda e: self.send_message())  # Send on Enter

        send_btn = tk.Button(input_frame, text="Send", command=self.send_message)
        send_btn.pack(side='left', padx=5)

        # Status label
        self.status = tk.Label(self.root, text="Connected ✓", fg='green')
        self.status.pack(pady=5)

    def _wait_server(self):
        """Server waits for client (background thread)"""
        try:
            self.net.wait_for_client()
            self.display("✓ Client connected!")
            self.receive_loop()
        except Exception as e:
            self.display(f"❌ Error: {e}")

    def send_message(self):
        """Encrypt and send message"""
        msg = self.entry.get().strip()
        if not msg:
            return

        try:
            encrypted = encrypt(self.key, msg)
            self.net.send(encrypted)
            self.display(f"You: {msg}")
            self.entry.delete(0, 'end')
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send: {e}")

    def receive_loop(self):
        """Continuously receive messages (background thread)"""
        while self.running:
            try:
                data = self.net.receive()
                if not data:
                    break
                msg = decrypt(self.key, data)
                self.display(f"Peer: {msg}")
            except Exception as e:
                self.display(f"❌ Receive Error: {e}")
                break

    def display(self, msg):
        """Add message to chat box"""
        self.chat_box.config(state='normal')
        self.chat_box.insert('end', msg + '\n')
        self.chat_box.see('end')  # Auto-scroll to bottom
        self.chat_box.config(state='disabled')

    def on_closing(self):
        """Clean up when closing"""
        self.running = False
        self.net.close()
        self.root.destroy()