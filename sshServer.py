import os
import sys
import socket
import threading
import paramiko

CWD = os.path.dirname(os.path.realpath(__file__))
HOST_KEY = paramiko.RSAKey(filename=os.path.join(CWD, 'test_rsa.key'))

class Server(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()
    
    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
    
    def check_auth_password(self, username, password):
        if username == 'tim' and password == 'sekret':
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

if __name__ == '__main__':
    server = '192.168.1.103'
    ssh_port = 2222
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((server, ssh_port))
        sock.listen(100)
        print('[+] Listening for connection ...')
        client, addr = sock.accept()
    except Exception as e:
        print(f'[-] Listen failed: {e}')
        sys.exit(1)
    else:
        print('[+] Got a connection!')

    bhSession = paramiko.Transport(client)
    bhSession.add_server_key(HOST_KEY)
    server = Server()
    bhSession.start_server(server=server)

    chan = bhSession.accept(20)
    print('[+] Authenticated!')
    print(chan.recv(1024))
    chan.send('Welcome to bh_ssh')
    while True:
        try:
            command = input('Enter command: ').strip('\n')
            if command != 'exit':
                chan.send(command)
                print(chan.recv(1024) + '\n')
            else:
                chan.send('exit')
                print('[*] Exiting ...')
                bhSession.close()
                raise Exception('exit')
        except KeyboardInterrupt:
            bhSession.close()