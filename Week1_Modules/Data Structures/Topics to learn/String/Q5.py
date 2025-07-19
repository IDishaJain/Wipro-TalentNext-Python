# 5. Given a string and an integer n, return a string made of n repetitions of the last n characters.
# Example: input "Wipro", 3 → "propropro"
string = input("Enter a string: ")
n = int(input("Enter n: "))
result = string[-n:] * n
print("Result:", result)