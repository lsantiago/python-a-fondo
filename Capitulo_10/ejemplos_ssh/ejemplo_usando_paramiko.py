import paramiko

if __name__ == '__main__':
    cliente = paramiko.client.SSHClient()
    cliente.load_system_host_keys()
    cliente.connect('192.168.1.148', username='ubuntu', password='pass')
    stdin, stdout, stderr = cliente.exec_command('ls -l')
    print(stdout.read().decode())
    stdin, stdout, stderr = cliente.exec_command('pwd')
    print(stdout.read().decode())
    stdin, stdout, stderr = cliente.exec_command('ls -l /')
    print(stdout.read().decode())
    stdin, stdout, stderr = cliente.exec_command('hostnamectl')
    print(stdout.read().decode())
    stdin, stdout, stderr = cliente.exec_command('iostats')
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = cliente.exec_command('ps -eo pcpu,pid,user,args | sort -k 1 -r | head -10')
    print(stdout.read().decode())
    cliente.close()
