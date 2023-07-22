#filter out the data from dictionary and store output in the dictionary
#filter out the person whose salaries in between 20k-30k
salary={'Abdeali': 20000,'Ali' :40000,'Kazim': 25000,'Katrina': 50000,'sarah': 27000}
data={k:v for (k,v) in salary.items() if v>20000 if v<30000}
print(data)