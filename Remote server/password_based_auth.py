import paramiko
server="192.168.100.230"
user="centos8"
password=""
command="df -Th"
client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=server,username=user,password=password)
stdin, stdout, stderr=client.exec_command(command=command)
output=stdout.read().decode()
print(output)





