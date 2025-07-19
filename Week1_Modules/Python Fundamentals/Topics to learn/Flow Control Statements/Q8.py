# 8. Print sum of digits of a number
num = int(input("Enter a number: "))
sum_digits = 0
temp = num
while temp > 0:
    sum_digits += temp % 10
    temp //= 10
print(f"Sum of digits of {num} is: {sum_digits}")