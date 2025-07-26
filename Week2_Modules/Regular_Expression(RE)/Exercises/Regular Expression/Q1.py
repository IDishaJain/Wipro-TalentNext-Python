# Write a program to find check if a string has only octal digits. Given string ['789','123','004']

strings = ['789', '123', '004']

for s in strings:
    if all(char in '01234567' for char in s):
        print(f"{s} is octal")
    else:
        print(f"{s} is not octal")
