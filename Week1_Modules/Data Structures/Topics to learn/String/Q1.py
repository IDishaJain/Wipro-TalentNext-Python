# 1. Write a program to count the number of upper and lower case letters in a String.
string = input("Enter a string: ")
upper = sum(1 for c in string if c.isupper())
lower = sum(1 for c in string if c.islower())
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")