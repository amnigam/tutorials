import struct 
import socket 

# Data that client wants to send
host_name = 'DESKTOP-THQHGKO'
os_name = 'Microsoft Windows 10 Pro'
owner = 'Amit Nigam' 
memory = 64
memory_unit = 'GB' 

data_stream = struct.pack('15s 25s 15s i 2s', host_name.encode(), os_name.encode(), owner.encode(), memory, memory_unit.encode()) 
print(f'[+] Data Stream is: {data_stream}') 

# Setup the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # Set Internet TCP Socket
client.connect( ('localhost', 9000))            # Connect on the server
client.send(data_stream) 
client.close() 
