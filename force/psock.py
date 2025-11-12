import socket

# Configure the server's IP address and port
server_ip = 'localhost'  # Change it to the appropriate IP address
server_port = 5000

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server's IP address and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections
server_socket.listen(1)
print('Server is listening on {}:{}'.format(server_ip, server_port))

# Accept a client connection
client_socket, client_address = server_socket.accept()
print('Client connected:', client_address)

while True:
    # Receive data from the client
    received_data = client_socket.recv(1024).decode()

    if received_data == 'quit':
        # Close the connection when 'quit' is received
        client_socket.close()
        print('Client disconnected')
        break
    else:
        # Process the received data (in this case, simply echo back)
        print('Received from MATLAB:', received_data)
        
        # Modify the received data (e.g., convert to uppercase)
        modified_data = received_data.upper()
        
        # Send the modified data back to the client (MATLAB)
        client_socket.send(modified_data.encode())
