import socket
import struct

class Server:
    def __init__(self, host='0.0.0.0', port=5000):  # Changed to 0.0.0.0
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((host, port))
        self.server.listen(1)
        self.conn = None
        print(f"[SERVER] Listening on ALL interfaces on port {port}")
        print(f"[SERVER] Other laptops should connect to: <YOUR_IP>:{port}")

    def wait_for_client(self):
        """Wait for a client to connect"""
        self.conn, addr = self.server.accept()
        print(f"[SERVER] Client connected from {addr}")

    def send(self, data: bytes):
        """Send encrypted data to client"""
        length = len(data)
        self.conn.sendall(struct.pack('!I', length) + data)

    def receive(self) -> bytes:
        """Receive encrypted data from client"""
        length_data = self.conn.recv(4)
        if not length_data:
            return b''
        length = struct.unpack('!I', length_data)[0]
        return self.conn.recv(length)

    def close(self):
        if self.conn:
            self.conn.close()
        self.server.close()


class Client:
    def __init__(self, host='localhost', port=5000):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.conn.connect((host, port))
            print(f"[CLIENT] Connected to {host}:{port}")
        except ConnectionRefusedError:
            print("[CLIENT] Could not connect to server. Is it running?")
            raise

    def send(self, data: bytes):
        """Send encrypted data to server"""
        length = len(data)
        self.conn.sendall(struct.pack('!I', length) + data)

    def receive(self) -> bytes:
        """Receive encrypted data from server"""
        length_data = self.conn.recv(4)
        if not length_data:
            return b''
        length = struct.unpack('!I', length_data)[0]
        return self.conn.recv(length)

    def close(self):
        self.conn.close()