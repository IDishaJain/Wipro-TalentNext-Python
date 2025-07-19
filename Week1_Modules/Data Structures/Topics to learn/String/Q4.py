# 4. Given a string, if first or last character is 'x', return string without those 'x',
# else return string unchanged.
string = input("Enter a string: ")
if string.startswith('x'):
    string = string[1:]
if string.endswith('x'):
    string = string[:-1]
print("Modified String:", string)
