with open("E:\\Knowledge_Hub\\Devops\\Python_Automation\\Notes\\Practice\\file1.txt", "r") as f:
    file_content=f.readline()
    while file_content:
        print(file_content, end='')
        file_content = f.readline()
f.close()