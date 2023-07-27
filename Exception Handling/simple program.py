try:
    a=2
    num=input("Enter number: ") #here input type is string so will get error while adding with 2 which is integer
    print(f"sum of {a} and {num} is: {a+num}")
except TypeError:
    print(f"invalid input, Kindly enter integers only!")
finally:
    print("program executed")