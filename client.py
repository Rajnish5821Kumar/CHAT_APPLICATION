import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.28.228", 12345)) # Connect to server
message = input("Enter message: ") # Get user input
client_socket.send(message.encode()) # Send message to server

while True:
        response = client_socket.recv(1024).decode() # Receive data
        print(f"Server: {response}")
        message = input("Enter message: ")
        if message.lower() == 'exit':
            print("Exiting...")
            break
        else:
            client_socket.send(message.encode()) # Send message

       
client_socket.close()