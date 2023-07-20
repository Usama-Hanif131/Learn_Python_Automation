#Python Program to Check if a Number is Positive, Negative or 0
num=eval(input("Enter a number: "))
if num > 0:
    print(f"{num} is positive!")
elif num < 0:
    print(f"{num} is negative!")
else:
    print("Number is zero !")
