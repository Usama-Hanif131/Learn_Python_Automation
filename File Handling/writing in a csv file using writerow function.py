import csv
path="E:\\Knowledge_Hub\\Devops\\Python_Automation\\Notes\\Practice\\data.csv"
server1=["ubuntu","192.168.0.23","python 3.11"]
server2=["Centos8","192.168.12.243","python 2.7"]
with open(path,'w', newline='') as f:
    file_writer=csv.writer(f)
    file_writer.writerow(server1)
    file_writer.writerow(server2)
f.close()