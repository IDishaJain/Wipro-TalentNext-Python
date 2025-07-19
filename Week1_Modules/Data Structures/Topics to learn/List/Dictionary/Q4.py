# 4. Write a program to iterate over a dictionary using for loop and print

my_dict = {'a': 100, 'b': 200, 'c': 300}
print("Keys:")
for key in my_dict.keys():
    print(key)
print("Values:")
for value in my_dict.values():
    print(value)
print("Keys and Values:")
for key, value in my_dict.items():
    print(f"{key} : {value}")