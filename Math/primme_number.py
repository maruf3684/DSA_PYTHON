
# A prime number is a natural number greater than 1 that has exactly two distinct positive divisors:
# 	•	1
# 	•	Itself


import math

def check_prime(num):
    start = num-1
    while start > 1:
        if num % start == 0:
            return False
        start -= 1
    return True

print(check_prime(3))



def check_prime_efficiant(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

print(check_prime_efficiant(3))

