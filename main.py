import tkinter as tk
from tkinter import simpledialog, messagebox
from ui import ChatApp
from network import Server, Client

def main():
    root = tk.Tk()
    root.withdraw()
    
    role = simpledialog.askstring("Chat", 'Type "server" or "client":')
    
    if role == 'server':
        host = simpledialog.askstring("Server", "Enter host (default: localhost):", initialvalue="localhost")
        port = simpledialog.askinteger("Server", "Enter port (default: 5000):", initialvalue=5000)
        app_role = 'server'
        net_kwargs = {'host': host, 'port': port}
    
    elif role == 'client':
        host = simpledialog.askstring("Client", "Enter server host:", initialvalue="localhost")
        port = simpledialog.askinteger("Client", "Enter server port:", initialvalue=5000)
        app_role = 'client'
        net_kwargs = {'host': host, 'port': port}
    
    else:
        messagebox.showerror("Error", "Invalid choice!")
        root.destroy()
        return
    
    root.deiconify()
    root.title(f"Secure Chat - {role.upper()}")
    root.geometry("600x600")
    
    try:
        app = ChatApp(root, role=app_role, net_kwargs=net_kwargs)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"Failed: {e}")
        root.destroy()

if __name__ == "__main__":
    main()