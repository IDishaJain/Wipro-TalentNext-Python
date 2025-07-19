# Count frequency of a user-entered word in the file

word = input("Enter word to count: ")
with open("IO Operations\Topic to learn\sample.txt", "r") as file:
    content = file.read().split()
count = content.count(word)
print(f"The word '{word}' appears {count} times.")