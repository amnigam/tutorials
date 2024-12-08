import struct 
import socket 
from clean import cleanString

# Objective of this script is to demonstrate how struct can be leveraged to pass data in a network. 
# This script sets up a server on localhost at port 9000. 
# It unpacks data in a pre-defined template between client & server. 

# Setup the server 
HOST = 'localhost' 
PORT = 9000
DATA_SIZE=1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Internet socket with TCP
s.bind((HOST, PORT))     # Bind to Localhost & port 9000
s.listen(5)                      # Listen with a backlog of 5. 5 connections can be queued; 6th dropped until queue is free.

try:
    while True: 
        client, addr = s.accept()       # Upon connection, extract address & client object
        print(f'[+] Connection received from: {addr}') 
        data = client.recv(DATA_SIZE)   # Data will be a struct. 

        # Pre-defined struct template => 15s 25s 15s i 2s
        host, os, owner, memory, memory_unit = struct.unpack('15s 25s 15s i 2s', data) 
        print('[+] Received Host Name: ', cleanString(host))
        print('[+] OS Name is: ', cleanString(os)) 
        print('[+] Owner\'s name is: ', cleanString(owner)) 
        print(f'[+] Memory Capacity is: {memory}') 
        print('[+] Memory Capacity Unit is: ', cleanString(memory_unit))
        print('------------------------------------------------------------------------------') 
        client.close()      # Close connection with client. 
except KeyboardInterrupt:
    print('Shutting down server...') 
    s.close() 

