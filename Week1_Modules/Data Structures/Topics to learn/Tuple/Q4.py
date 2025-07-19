# 4. Write a program to find the index of an item in a tuple.
my_tuple = (5, 10, 15, 20, 25)
element = int(input("Enter element to find index: "))
if element in my_tuple:
    index = my_tuple.index(element)
    print(f"Index of {element}:", index)
else:
    print(f"{element} not found in the tuple.")