from datetime import datetime
import paramiko
server="192.168.100.230"
user="centos8"
private_key_path=r"" #path of hosts machine private key
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=server,username=user,key_filename=private_key_path)
stdin, stdout, stderr=ssh.exec_command("free -m")
output=stdout.readlines()
#extract memory information
memory_info=output[1]
memory_info_list=memory_info.split()
Available_memory=memory_info_list[6]
Total_memory=memory_info_list[1]
Memory_used=memory_info_list[2]
#extract swap information
swap_info=output[2]
swap_info_list=swap_info.split()
Total_swap=swap_info_list[1]
Available_swap=swap_info_list[3]
swap_used=swap_info_list[2]
#setting current date and time
time=datetime.now()
current_time=time.strftime("%I:%M:%S %p")
current_date=time.strftime("%A %m, %Y")

#setting up Alerts conditions
if int(Available_memory) < 500:
    alert="Alert: Memory is very low , kindly check processes which consume memory"
    if int(Available_swap) < 1500:
        alert="Alert: Memory is very low , kindly check processes which consume memory. \
\nAlso we notice the usage of swap memory, kinldly immediately take action \
\nAs some processes consume huge ammount of memory."
else:
    alert="Memory is enough, there is no worries!"

#setting up message
runtime_memory_information=f"""
Memory Runtime details on {current_date} at {current_time}:

Total Memory: {Total_memory} MB
Availble Memory:{Available_memory} MB
Used Memory: {Memory_used} MB

Total Swap: {Total_swap} MB
Available swap: {Available_swap} MB
Used swap: {swap_used} MB

{alert}
\n\n
"""
sftp=ssh.open_sftp()
file=sftp.open(r"/home/centos8/Desktop/server.txt","a")
file.write(runtime_memory_information)
sftp.close()
ssh.close()
print("Script Successfully Executed :)")