try:
    # Code block where an exception might occur
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result1 = num1 + num2
    result2= num1 / num2
    print(f"Sum={result1}\nDivison={result2}")    
except ValueError:
    print("Error: Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Operation completed.")
