# accept two number from user and perform division
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter integers only.")
else:
    print("Result:", result)
