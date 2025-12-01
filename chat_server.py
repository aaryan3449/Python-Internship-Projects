# chat_server.py

import socket
import threading

HOST = "127.0.0.1"   # localhost (same computer)
PORT = 55555         # you can change this if needed

clients = []
names = []

def broadcast(message, _client=None):
    """Send message to all connected clients"""
    for client in clients:
        if client != _client:
            try:
                client.send(message)
            except:
                pass

def handle_client(client):
    """Handle messages from a single client"""
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            broadcast(message, client)
        except:
            break

    # remove client when it leaves
    if client in clients:
        index = clients.index(client)
        clients.remove(client)
        name = names[index]
        names.remove(name)
        print(f"{name} left the chat.")
        broadcast(f"{name} left the chat.\n".encode("utf-8"))
        client.close()

def receive_connections():
    """Main loop for accepting new clients"""
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("NAME".encode("utf-8"))
        name = client.recv(1024).decode("utf-8")
        names.append(name)
        clients.append(client)

        print(f"Name of client is {name}")
        broadcast(f"{name} joined the chat.\n".encode("utf-8"))
        client.send("You are connected to the server.\n".encode("utf-8"))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

# create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server is running...")
print(f"Listening on {HOST}:{PORT}")
receive_connections()
