# check palindrome number
num = int(input("Enter a number to check palindrome: "))
reverse = 0
temp = num

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if num == reverse:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")