# 3. Check if two numbers have the same last digit
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a % 10 == b % 10:
    print("True")
else:
    print("False")