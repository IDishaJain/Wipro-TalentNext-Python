# 5. Write a program to prepare a dictionary where the keys are numbers between 1 and 15
# (both included) and the values are squares of the keys.
square_dict = {}
for num in range(1, 16):
    square_dict[num] = num * num
print("Squares Dictionary:", square_dict)