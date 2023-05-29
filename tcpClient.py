import socket
target_host = "127.0.0.1" # Host
target_port = 9998 # Port (Must be an integer) 80 is the default port for HTTP

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET is the IPv4 address family, SOCK_STREAM is the TCP protocol

# Connect the client
client.connect((target_host, target_port)) # Connect to the server

# Send data
# This is an HTTP GET request to the root directory of google.com using HTTP version 1.1, with a host header specifying the hostname.
# The \r\n characters are used to separate the different parts of the HTTP request message.
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n") # Send some data to the server (b'' is for bytes, to avoid encoding errors)

# Receive data
response = client.recv(4096) # Receive some data (4096 is the buffer size)

# Print data
print(response) # Print the response
client.close() # Close the connection