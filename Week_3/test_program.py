"""Question 1: count_letters"""
def count_letters(s, letter):
    count = 0
    i = 0
    for i in range(len(s)):
        if s[i] == letter:
            count += 1
    return count



"""Testing Question 1 implementation"""
def test_count_letters():
    print("Testing count_letters()...", end="")
    assert(count_letters("Hello", "l") == 2)
    assert(count_letters("apple", "a") == 1)
    assert(count_letters("Hi", "h") == 0) # case sensitive!
    assert(count_letters("More letters", "e") == 3)
    print("...done!")

  
  
  
"""Question 2: digit_sum"""
def digit_sum(n):
    n = abs(n)
    sum = 0
    while (n != 0):
        sum = sum + (n%10)
        n = n//10
    return sum
  
  
"""Testing Question 2 implementation"""  
def test_digit_sum():
    print("Testing digit_sum()...", end="")
    assert(digit_sum(3) == 3)
    assert(digit_sum(16) == 7)
    assert(digit_sum(1234) == 10)
    assert(digit_sum(0) == 0)
    assert(digit_sum(-35) == 8)
    print("... done!")

  

    
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
  
  
  
   
"""Question 4: alternating_sum"""
def alternating_sum(L):
    sum = 0
    for i in range(len(L)):
        if (i % 2 == 0):
            sum += L[i]
        else:
            sum -= L[i]
    return sum



  
"""Testing Question 4 implementation"""  
def test_alternating_sum():
    print("Testing alternating_sum()...", end="")
    assert(alternating_sum([7]) == 7)
    assert(alternating_sum([1, 2]) == -1)
    assert(alternating_sum([1, 3, 1]) == -1) 
    assert(alternating_sum([3, 2, 1]) == 2)
    assert(alternating_sum([8, 0, 0, 0]) == 8)
    assert(alternating_sum([5, 5, 5, 5]) == 0)
    print("... done!")
  

        

"""Question 5: has_property_309"""
def digit_present(num, digit):
    while num > 0:
        if digit == num%10: return True
        num //= 10
    return False
 
def has_property_309(n):
    fifth_power = n**5
    for i in range(10):
        if not digit_present(fifth_power, i):
            return False
    return True



"""Testing Question 5 implementation"""  
def test_has_property_309():
    print("Testing has_property_309()...", end="")
    assert(has_property_309(309) == True)
    assert(has_property_309(371) == False)
    assert(has_property_309(575) == True)
    assert(has_property_309(17) == False)
    assert(has_property_309(0) == False)
    assert(has_property_309(462) == True)
    print("... done!")



  
"""Question 6: nth_property_309"""
def nth_property_309(n):
    num_found = 0
    i = 0
    while num_found <= n:
        i += 1
        if has_property_309(i):
            num_found += 1
    return i




"""Testing Question 6 implementation"""  
def test_nth_property_309():
    print("Testing nth_property_309()...", end="")
    assert(nth_property_309(0) == 309)
    assert(nth_property_309(1) == 418)
    assert(nth_property_309(2) == 462)
    assert(nth_property_309(6) == 662)
    assert(nth_property_309(9) == 713)
    print("... done!")
  

  
  
"""Question 7: Fix the Code"""
# Remove the triple quotes from the following block of code to run this!
def factorial(n):
    counter = 1
    total = n
    while counter < n:
        total *= (n-counter)
        counter += 1
    return total

def test_factorial():
    print("Testing factorial()...", end="")
    assert(factorial(3) == 6)
    assert(factorial(5) == 120)
    assert(factorial(1) == 1)
    assert(factorial(8) == 40320)
    print("...done!")


  

if __name__ == '__main__':
    test_count_letters()
    test_digit_sum()
    test_every_other()
    test_alternating_sum()
    test_has_property_309()
    test_nth_property_309()    
    test_factorial()         # uncomment for Q7