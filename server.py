import socket
# from psock import function1
# import re
import bpy
import bpy.ops
import os
import sys
import numpy as np


dir = os.path.dirname(bpy.data.filepath)
if not dir in sys.path:
    sys.path.append(dir )
print(dir)
import first_render
from first_render import draw_polyline

print(dir)


server_ip = 'localhost' 
 # Change it to the appropriate IP address
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
count = 0

while True:
    # Receive data from the client
#    client_socket, client_address = server_socket.accept()
#    print('Client connected:', client_address)
    desired_length = 1970
    received_data = ""
    termination_character = "/"
    # while len(received_data)<desired_length:
    #        # print(received_data)
    #        data = client_socket.recv(desired_length-len(received_data))
    #        received_data += data.decode()
    #        if termination_character in received_data:
    #            break
    while True:
           # print(received_data)
           data = client_socket.recv(1024)
           received_data += data.decode()
           if termination_character in received_data:
               break
           if len(data) == 0:
                break
    received_data = received_data.split(termination_character)[0]
    string_p = received_data.split("Position_")[1:]
    string_R = received_data.split("Rotation_")[1:]

    result_pos = []
    result_rot = []
        
    for position in string_p:
        values = position.split(" ")
        cordinates = values[1].split("(")[1].split(",")
        x = float(cordinates[0])
        y = float(cordinates[1])
        z = float(cordinates[2])
        result_pos.append((x,y,z))

    for rotation in string_R:
        values = rotation.split(" ")
        cordinates = values[1].split("(")[1].split(",")
        x = float(cordinates[0])
        y = float(cordinates[1])
        z = float(cordinates[2])
        result_rot.append((x,y,z))

    print(result_pos,result_rot)
    result_rot = result_rot[::-1]
    
    check = draw_polyline(result_pos,result_rot,str(count))
    if check:
        # Process the received data (in this case, simply echo back)
        # print('Received from MATLAB:', received_data)
        modified_data = "Rendered"
        # Send the modified data back to the client (MATLAB)
        client_socket.send(modified_data.encode())
        count = count+1
    
    else:
        client_socket.close()
        print('Client disconnected')
        break
        
