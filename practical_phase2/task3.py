myfiles = ["abd.txt", "abc.csv", "test.txt", "ali.txt", "abdeali.csv"]
updated_iles=[i.upper() for i in myfiles if i!="abdeali.csv"]
print(updated_iles)