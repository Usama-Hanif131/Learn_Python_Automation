#pickup the elite empoyees in company whose salary is greater than 30000 
salary = [
['Abdeali', 20000],
['Ali', 30000],
['Kazim', 25000],
['Katrina', 50000],
['sarah', 27000]
]
elite_employees=[i for i in salary if i[1] >= 30000]
print(elite_employees)