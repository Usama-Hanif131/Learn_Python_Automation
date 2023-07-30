with open("E:\\Knowledge_Hub\\Devops\\Python_Automation\\Notes\\Practice\\file1.txt", "a") as f:
    f.write("\nHere we append something")
f.close()
with open("E:\\Knowledge_Hub\\Devops\\Python_Automation\\Notes\\Practice\\file1.txt", "r") as g:
    print(g.read())
g.close()
