# 3. Write a function to calculate and return the factorial of a number (non-negative integer).
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) 
