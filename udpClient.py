import socket
target_host = "127.0.0.1" # Host
target_port = 80 # Port (Must be an integer) 80 is the default port for HTTP

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # SOCK_DGRAM is for UDP

# Send some data
client.sendto(b"AAABBBCCC", (target_host, target_port)) # sendto() takes a string and a tuple

# Receive some data
data, addr = client.recvfrom(4096) # 4096 is the buffer size

# Print the data
print(data)

