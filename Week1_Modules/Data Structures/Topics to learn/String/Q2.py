# 2. Write a program to check whether a given String is Palindrome or not.
string = input("Enter a string to check palindrome: ")
if string == string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")