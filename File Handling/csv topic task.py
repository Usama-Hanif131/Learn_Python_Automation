"""program to read data from serverhealth.csv file and filter out 
the servers list that has RAM less than 10GB, write that data in a new csv file
"""
import csv
file_content=[]
path="E:\\Knowledge_Hub\\Devops\\Python_Automation\\Lecture 38 servershealth.csv"
with open(path,"r") as f:
    content=csv.reader(f)
    header=next(content)
    for each_line in content:
        size=int(each_line[4].strip("GB"))
        if size < 10:
            file_content.append(each_line)
f.close()

with open("E:\\Knowledge_Hub\\Devops\\Python_Automation\\Notes\\Practice\\newfile.csv", "a", newline="") as g:
    file_writer=csv.writer(g)
    file_writer.writerow(header)
    file_writer.writerows(file_content)
g.close()