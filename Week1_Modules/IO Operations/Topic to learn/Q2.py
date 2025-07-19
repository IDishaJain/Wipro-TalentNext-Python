# Read first n lines from a .txt file (n from user)

n = int(input("Enter number of lines to read: "))
with open("IO Operations\Topic to learn\sample.txt", "r") as file:
    for _ in range(n):
        print(file.readline(), end='')