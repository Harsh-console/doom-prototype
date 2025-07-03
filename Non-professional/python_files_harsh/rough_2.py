import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5555))  # Listen on all interfaces
server.listen()

clients = []

def handle_client(client):
    while True:
        try:
            data = client.recv(1024)
            broadcast(data, client)
        except:
            clients.remove(client)
            break

def broadcast(data, sender):
    for c in clients:
        if c != sender:
            c.send(data)

print("Server started...")
while True:
    client, addr = server.accept()
    print(f"Connected with {addr}")
    clients.append(client)
    threading.Thread(target=handle_client, args=(client,)).start()
