#writing in a file
with open("E:\\Knowledge_Hub\\Devops\\Python_Automation\\Notes\\Practice\\file1.txt","w") as f:
    f.write("Hallo, ich bin Osama!")
f.close()
#reading file
with open("E:\\Knowledge_Hub\\Devops\\Python_Automation\\Notes\\Practice\\file1.txt","r") as g:
    print(g.read())
g.close()
