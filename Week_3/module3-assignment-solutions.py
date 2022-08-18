# Assignment 3.1 Solutions
###################################################
# Q1
###################################################

def count_letters(s, letter):
    count = 0
    for c in s:
        if c == letter:
            count += 1
    return count

###################################################
# Q2
###################################################
 
def digit_sum(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n%10
        n //= 10
    return total

###################################################
# Q3
###################################################

def every_other(s, start):
    return s[start::2]

###################################################
# Q4
###################################################

def alternating_sum(L):
    total = 0
    for i in range(len(L)):
        if i % 2 == 0:
            total += L[i]
        else:
            total -= L[i]
    return total

###################################################
# Q5
###################################################

def has_digit(n, d):
    while n > 0:
        if d == n%10: return True
        n //= 10
    return False
 
def has_property_309(n):
    fifth_power = n**5
    for d in range(10):
        if not has_digit(fifth_power, d):
            return False
    return True

###################################################
# Q6
###################################################

def nth_property_309(n):
    num_found = 0
    guess = 0
    while num_found <= n:
        guess += 1
        if has_property_309(guess):
            num_found += 1
    return guess

###################################################
# Q7
###################################################

def factorial(n):
    counter = 1
    total = n
    while counter < n:
        total *= (n-counter)
        counter += 1
    return total

# Changes:
# 1. Start counter at 1
# 2. Loop guard should be < instead of <=
# 3. Increment counter by 1 inside the loop

###################################################
# Q8 (spicy)
###################################################

def gcd(x, y):
    while y != 0:
        temp_y = y
        y = x%y
        x = temp_y
    return x

###################################################
# Q9 (spicy)
###################################################

def longest_digit_run(n):
    n = abs(n)
    longest_run = 1
    longest_digit = n%10
    curr_run = 1
    curr_digit = n%10
    n //= 10
    while n > 0:
        digit = n%10
        if digit == curr_digit:
            curr_run += 1
        else:
            if curr_run > longest_run:
                longest_run = curr_run
                longest_digit = curr_digit
            elif curr_run == longest_run and curr_digit < longest_digit:
                longest_run = curr_run
                longest_digit = curr_digit
            curr_run = 1
            curr_digit = digit
        n //= 10
    return longest_digit