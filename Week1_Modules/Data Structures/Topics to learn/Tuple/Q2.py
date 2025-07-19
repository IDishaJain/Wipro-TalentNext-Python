# 2. Write a program to check whether an element exists in a tuple or not.
my_tuple = (1, 2, 3, 4, 5)
element = int(input("Enter element to search: "))
if element in my_tuple:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")