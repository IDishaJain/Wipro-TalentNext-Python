#  Accept input from user and append to a .txt file

text = input("Enter text to append: ")
with open("IO Operations\Topic to learn\sample.txt", "a") as file:
    file.write(text + '\n')
print("Text appended successfully.")