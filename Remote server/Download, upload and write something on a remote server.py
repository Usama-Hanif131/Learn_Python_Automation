import paramiko
private_key_path=r"C:\Users\usa35\.ssh\id_rsa"
server="192.168.100.230"
user="centos8"
client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=server,username=user,key_filename=private_key_path)
sftp=client.open_sftp()
#downloading from remote server
sftp.get(r"/home/centos8/sample.txt",r"E:\Knowledge_Hub\Devops\server.txt")
#uploading on remote server
sftp.put(r"E:\Knowledge_Hub\Devops\server.txt", r"/home/centos8/Desktop/server.txt")
#append text on remote server file
file=sftp.open(r"/home/centos8/Desktop/server.txt","a")
file.write("Hello, we have plan something for Ansible!\n")
sftp.close()
client.close()


