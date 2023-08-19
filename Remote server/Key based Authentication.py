import paramiko
hostname="192.168.100.230"
username="centos8"
pk_path=r"" #path of hosts machine private key
command="df -Th"
client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname, username=username, key_filename=pk_path)
stdin1, stdout1, stderr1=client.exec_command(command)
#dealing output as a string
output1=stdout1.read().decode()
print("outpu1")
print(output1)
# dealing output as a list
stdin2, stdout2, stderr2=client.exec_command(command)
output2=stdout2.readlines()
print("outpu2")
for i in output2:
    print(i.strip("\n"))