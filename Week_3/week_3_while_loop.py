def get_positive_int():
    user_input = 0       
    while (user_input <= 0):     
        user_input = int(input("Enter a positive integer: "))
    return user_input

# positive_int = get_positive_int()
# print("User entered:", positive_int)

def my_print(s, num):
    counter = 1
    while(counter <= num):
        print(s)
        counter += 1

# my_print("hello", 5)

def ask_and_print():
    user_str = input("Enter what you would like to print: ")
    user_num = get_positive_int()
    my_print(user_str, user_num)

ask_and_print()


###### just test for while
x = 0

while x < 10:

   x += 3

print(x)

##############

def multiple_subtracts(x, y):
  while (x > 0):
    x = x - y
  return x

print(multiple_subtracts(5, 3))
print(multiple_subtracts(8, 2))
print(multiple_subtracts(6, 7))
print(multiple_subtracts(-2, 4))


def sum_to_n(n):
    counter = 1
    total = 0       
    while(counter <= n):
        total += counter
        counter += 1
    return total

print(sum_to_n(4))

def sum_from_m_to_n(m, n):
    index = m
    result = 0       
    while(index <= n):
        result += index
        index += 1
    return result

print(sum_from_m_to_n(3, 5))

def sum_of_odds_v1(m, n):
    result = 0
    index = m
    while (index <= n):
        if (index % 2 == 1): 
            result += index
        index += 1
    return result

print(sum_of_odds_v1(2, 7))

def sum_of_odds_v2(m, n):
    if (m % 2 == 0):
        m += 1
    result = 0
    index = m
    while (index <= n):
        result += index
        index += 2
    return result

print(sum_of_odds_v2(2, 7))



# original example
def sum_of_evens(m, n):
 if (m % 2 != 0):
   m += 1
 result = 0
 index = m
 while (index <= n):
   result += index
   index += 2
 return result
 
print(sum_of_evens(3, 8))


def leftmost_digit(n):
    n = abs(n)
    while (n >= 10):
        n = n // 10    
    return n

def test_leftmost_digit():
    print("Testing leftmost_digit...", end=" ")
    assert(leftmost_digit(0) == 0)
    assert(leftmost_digit(1) == 1)
    assert(leftmost_digit(2) == 2)
    assert(leftmost_digit(10) == 1)
    assert(leftmost_digit(19) == 1)
    assert(leftmost_digit(900) == 9)
    assert(leftmost_digit(15250) == 1)
    assert(leftmost_digit(500000) == 5)
    assert(leftmost_digit(-1) == 1)
    assert(leftmost_digit(-2) == 2)
    assert(leftmost_digit(-10) == 1)
    assert(leftmost_digit(-19) == 1)
    assert(leftmost_digit(-900) == 9)
    assert(leftmost_digit(-15250) == 1)
    assert(leftmost_digit(-500000) == 5)
    print("Passed!")

test_leftmost_digit()


def is_awesome(n):
    return (n % 3 == 0) or (n % 5 == 0)

def nth_awesome(n):
    num_found = 0
    guess = 0
    while (num_found < n):
        guess += 1
        if (is_awesome(guess)):
            num_found += 1
    return guess

def test_is_awesome():
    print("Testing is_awesome...", end=" ")
    assert(not is_awesome(1))
    assert(not is_awesome(2))
    assert(is_awesome(3))
    assert(not is_awesome(4))
    assert(is_awesome(5))
    assert(is_awesome(6))
    assert(not is_awesome(7))
    assert(is_awesome(100))
    assert(not is_awesome(101))
    assert(is_awesome(102))
    print("Passed.")

test_is_awesome()

def test_nth_awesome():
    print("Testing nth_awesome...", end=" ")
    assert(nth_awesome(1) == 3)
    assert(nth_awesome(2) == 5)
    assert(nth_awesome(3) == 6)
    assert(nth_awesome(4) == 9)
    assert(nth_awesome(5) == 10)
    print("Passed.")

test_nth_awesome()

# Count digits function
def count_digits(n):
  n = abs(n)
  index = 0
  total = 0
  while n > 0:
    total += 1
    n //= 10
    print("Inside while:", n)
  return total
  
print(count_digits(14))

# prime number
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