import paramiko
hostname="192.168.100.230"
username="centos8"
pk_path=r"" #path of hosts machine private key
command="df -Th"
client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname, username=username, key_filename=pk_path)
stdin, stdout, stderr=client.exec_command(command)
output=stdout.readlines()
for i in output[1::]:
    index=i.split()[5].strip("%")
    if int(index) > 20:
        print(i.strip("\n"))
        
        
        