print(list(range(4)))
print(list(range(5, 10)))
print(list(range(2, 11, 3)))
print(list(range(2, -2, -1)))

lst = ["apples", "oranges", "mangoes", "bananas"]
print(lst[1])
print(lst[3])


## print a string using while and for loop

def my_print(s,num):
  input = 0
  for input in range(num):
    print(s)
    
my_print("hello",3)

# check is prime
def is_prime(num):
    if (num <= 1):
        return False
    for possible_factor in range(2, num):
        if (num % possible_factor == 0):
            return False
    return True

def test_is_prime():
    print("Testing is_prime...", end=" ")
    assert(not is_prime(1))
    assert(is_prime(2))
    assert(is_prime(3))
    assert(not is_prime(4))
    assert(is_prime(5))
    assert(not is_prime(6))
    assert(is_prime(251))
    print("Passed!")

test_is_prime()

def faster_is_prime(num):
    if (num <= 1):
        return False
    max_factor = round(num**0.5)
    for possible_factor in range(2, max_factor + 1):
        if (num % possible_factor == 0):
            return False
    return True

def test_faster_is_prime():
    print("Testing is_prime...", end=" ")
    assert(not faster_is_prime(1))
    assert(faster_is_prime(2))
    assert(faster_is_prime(3))
    assert(not faster_is_prime(4))
    assert(faster_is_prime(5))
    assert(not faster_is_prime(6))
    assert(faster_is_prime(251))
    assert(faster_is_prime(1000004249))
    assert(faster_is_prime(1000000000039))
    print("Passed!")

test_faster_is_prime()


"""Question 3: every_other"""
def every_other(s, start):
    return s[start::2]
  


  
"""Testing Question 3 implementation"""  
def test_every_other():
    print("Testing every_other()...", end="")
    assert(every_other("Hello", 0) == "Hlo")
    assert(every_other("blueberries", 3) == "eere")
    assert(every_other("banana", 1) == "aaa")
    assert(every_other("apple", 4) == "e")
    assert(every_other("eat", 4) == "")
    print("... done!")