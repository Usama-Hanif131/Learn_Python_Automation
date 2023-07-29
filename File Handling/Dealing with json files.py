#Read json file
with open("E:\\Knowledge_Hub\\Devops\\Python_Automation\\Notes\\Practice\\data.json", "r") as f:
    content=f.read()
    print(content)

#convert json file data into dictionary format
import json
with open("E:\\Knowledge_Hub\\Devops\\Python_Automation\\Notes\\Practice\\data.json", "r") as jf:
    mydict=json.load(jf)
    print(mydict)
f.close()