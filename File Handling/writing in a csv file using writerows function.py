import csv
path="E:\\Knowledge_Hub\\Devops\\Python_Automation\\Notes\\Practice\\data.csv"
mylist=[[1,'172.16.23.124','Unix','python 3.7'] ,[2,'192.168.19.234','ubuntu','Nagios']]
with open(path, "a",newline="") as f:
    file_writer=csv.writer(f)
    file_writer.writerows(mylist)
f.close()