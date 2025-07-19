# Indexing and positive/negative check from list

try:
    nums = [12, -4, 7, 0, -9, 15, -3, 8, -1, 5]
    index = int(input("Enter index (0-9): "))
    value = nums[index]
    if value > 0:
        print("Positive number")
    elif value < 0:
        print("Negative number")
    else:
        print("Zero")
except IndexError:
    print("Error: Index out of range.")
except ValueError:
    print("Error: Please enter a valid integer.")
