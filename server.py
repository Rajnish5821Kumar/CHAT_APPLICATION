import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.28.228", 12345)) # Bind server to IP and port
server_socket.listen(5) # Listen for 5 clients

print("Server is listening on port 12345...")
client_socket, client_address = server_socket.accept() # Accept a client
print(f"Connected to {client_address}")

while True:
    data = client_socket.recv(1024).decode() # Receive data from client
    if not data:
        break # Exit loop if no data received
    print(f"Client: {data}")

    message = input("Enter message: ") # Get user input
    if message.lower() == 'exit':
        print("Exiting...")
        break
    else:
        client_socket.send(message.encode()) # Send message to client

client_socket.close()
server_socket.close()