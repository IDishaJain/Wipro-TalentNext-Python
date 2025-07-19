# Student Average Marks Calculator

students = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}


name = input("Enter a name: ")

if name in students:
    marks = students[name]
    average = sum(marks) / len(marks)
    print(f"Average percentage mark: {average:.0f}")
    print(f"Marks for {name} are {marks} whose average is ({' + '.join(map(str, marks))}) / {len(marks)} => {average:.2f}")
else:
    print(f"Student '{name}' not found!")