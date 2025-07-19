#  Read file line by line and store each line into a list

with open("IO Operations\Topic to learn\sample.txt", "r") as file:
    lines = file.readlines()
print("Lines as list:", lines)