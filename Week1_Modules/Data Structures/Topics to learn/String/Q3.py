# 3. Given a string, return a new string made of n copies of the first 2 chars
# where n is the length of the string (length >=2).
# Example: "Wipro" → "WiWiWiWiWi"
string = input("Enter a string: ")
n = len(string)
result = string[:2] * n
print("Result:", result)