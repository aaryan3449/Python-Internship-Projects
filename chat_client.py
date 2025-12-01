# chat_client.py

import socket
import threading

HOST = "127.0.0.1"   # must match server
PORT = 55555         # must match server

name = input("Enter your name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    """Listen for messages from the server"""
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message == "NAME":
                client.send(name.encode("utf-8"))
            else:
                print(message, end="")   # message already has \n usually
        except:
            print("An error occurred. Closing connection.")
            client.close()
            break

def send_messages():
    """Send messages to the server"""
    while True:
        text = input("")
        message = f"{name}: {text}\n"
        try:
            client.send(message.encode("utf-8"))
        except:
            print("Connection closed.")
            break

# run both functions in parallel
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

write_thread = threading.Thread(target=send_messages)
write_thread.start()
