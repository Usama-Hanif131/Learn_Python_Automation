#filter out only those files that include "a" in thier names
myfiles = ["abd.txt", "abc.csv", "test.txt", "ali.txt", "abdeali.csv"]
newfiles=[]
for i in myfiles:
    if "a" in i:
        newfiles.append(i)
print(newfiles)