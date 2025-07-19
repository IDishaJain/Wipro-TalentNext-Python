# 4. Write a function that accepts a string and prints the number of upper and lower case letters in it.
def count_upper_lower(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")

count_upper_lower("HelloWorld")