#  Find the longest word in the file

with open("IO Operations\Topic to learn\sample.txt", "r") as file:
    words = file.read().split()
longest = max(words, key=len)
print("Longest word:", longest)