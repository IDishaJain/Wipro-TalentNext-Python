# 5. Write a function to print the even numbers from a given list.
def print_even_numbers(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    print("Even numbers:", even_numbers)

print_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])