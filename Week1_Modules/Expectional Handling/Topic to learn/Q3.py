# Accept file name and print contents if file exists
try:
    filename = input("Enter file name: ")
    with open(filename, "r") as file:
        content = file.read()
    print("File content:\n", content)
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Error:", e)
