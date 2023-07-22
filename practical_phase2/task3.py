#filter out files and make the output in upper case
myfiles = ["abd.txt", "abc.csv", "test.txt", "ali.txt", "abdeali.csv"]
updated_files=[i.upper() for i in myfiles if i!="abdeali.csv"]
print(updated_files)