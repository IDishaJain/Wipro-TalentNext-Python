# Accept 10 numbers and print sum of prime numbers among them
import sys

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

nums = list(map(int, sys.argv[1:]))
prime_sum = sum(num for num in nums if is_prime(num))
print("Sum of primes:", prime_sum)
