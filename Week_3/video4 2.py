# Try-It Exercise 3.3: While Loops and Problem-Solving Solutions:
# 1. 
def count_digits(n):
    n = abs(n)
    if n == 0: return 1
    total = 0
    while n > 0:
        total += 1
        n //= 10
    return total

# 2. C

# 3. 
def is_prime(num):
    if num < 2: return False
    for factor in range(2, num):
        if num%factor == 0: return False
    return True

def nth_prime(n):
    count = 0
    guess = 0
    while count <= n:
        guess += 1
        if is_prime(guess):
            count += 1
    return guess