import paramiko

def ssh_command(ip, port, user, password, cmd):
    client = paramiko.SSHClient()
    # client.load_host_keys('/home/justin/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=password)

    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('--- Output ---')
        for line in output:
            print(line.strip())
    client.close()

if __name__ == '__main__':
    import getpass
    # user = getpass.getuser()
    user = input('Username: ')
    password = getpass.getpass()

    ip = input('Enter Server IP: ') or '192.168.1.203'
    port = int(input('Enter Server Port: ') or 2222)
    cmd = input('Enter Command: ') or 'id'
    ssh_command(ip, port, user, password, cmd)