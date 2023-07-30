import json 
with open("E:\\Knowledge_Hub\\Devops\\Python_Automation\\Notes\\Practice\\task.json","r") as jf:
    data=json.load(jf)
jf.close()
mylist=[]
for i in range(len(data)):
    if data[i]["price"] > 1:
        mylist.append((data[i]["name"]))
print(f"The Fruits that has price below 1$ is:\n1) {mylist[0]}\n2) {mylist[1]}\n3) {mylist[2]}")