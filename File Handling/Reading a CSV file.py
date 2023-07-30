import csv
path="E:\\Knowledge_Hub\\Devops\\Python_Automation\\Lecture 37 servershealth.csv"
with open(path,"r") as f:
    data=csv.reader(f)
    for eachline in data:
        print(eachline)
f.close()