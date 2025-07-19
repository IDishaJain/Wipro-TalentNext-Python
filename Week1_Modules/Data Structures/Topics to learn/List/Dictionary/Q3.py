# 3. Write a program to check if a given key already exists in a dictionary.
sample_dict = {1: 'A', 2: 'B', 3: 'C'}
key = int(input("Enter a key to check: "))
if key in sample_dict:
    print(f"Key {key} exists.")
else:
    print(f"Key {key} does not exist.")