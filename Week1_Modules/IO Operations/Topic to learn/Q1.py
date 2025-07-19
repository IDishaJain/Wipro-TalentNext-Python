# Read entire content from a .txt file and display it

with open("IO Operations\Topic to learn\sample.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)