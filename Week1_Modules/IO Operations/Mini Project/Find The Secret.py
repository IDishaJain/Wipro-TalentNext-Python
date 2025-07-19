from collections import Counter

with open("IO Operations\Mini Project\message.txt", "r") as file:
    lines = file.readlines()

time = len(lines)
hour = time if time <= 12 else time - 12
suffix = "AM" if time <= 12 else "PM"

words = []
for line in lines:
    words.extend(line.strip().split())

count = Counter(words)
place = max(count.items(), key=lambda x: x[1])[0]

print(f"{hour} {suffix}")
print(f"{place} Street")
