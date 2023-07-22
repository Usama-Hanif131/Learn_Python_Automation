#find out maximum salaried person 
salary = [
['Abdeali', 20000],
['Ali', 30000],
['Kazim', 25000],
['Katrina', 50000],
['sarah', 27000]
]

max_salaried_person=[i for i in salary if i[1] > 30000]
print(max_salaried_person)