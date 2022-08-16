"""Question 1: get_grade"""
def get_grade(grade):
  
  if grade >= 90:
    return "A"
  elif grade >= 80 and grade <= 89:
    return "B"
  elif grade >= 70 and grade <= 79:
    return "C"
  elif grade >= 60 and grade <= 69:
    return "D"
  else:
    return "F"
  return
  

"""Testing Question 1 implementation"""
def test_get_grade():
  print("Testing get_grade()...", end="")
  assert(get_grade(0) == 'F')
  assert(get_grade(59) == 'F')
  assert(get_grade(63) == 'D')
  assert(get_grade(71) == 'C')
  assert(get_grade(80) == 'B')
  assert(get_grade(100) == 'A')
  print("...done!")

  
  
  
"""Question 2: pay_bill"""
def pay_bill(total, method):
  if method == "card" and total < 20:
    return (total + ((total*20)/100) + ((total*2)/100))
  elif method == "card" or method == "cash":
    return (total + ((total*20)/100))


   
"""Testing Question 2 implementation"""  
def test_pay_bill():
  print("Testing pay_bill()...", end="")
  assert(pay_bill(50, "cash") == 60.0)
  assert(pay_bill(15, "cash") == 18.0)
  assert(pay_bill(15, "card") == 18.3)
  assert(pay_bill(33, "card") == 39.6)
  assert(pay_bill(50, "card") == 60.0)
  print("... done!")

  """Question 3: split_bill"""
def split_bill(total, num_people):
  amount = (total + (20*total)/100)/num_people
  print("Each person pays " + str(amount) + " dollars.")

  
"""Testing Question 3 implementation"""  
def test_split_bill():
  print("Testing split_bill()...", end="")
  assert(split_bill(10, 3) == None)  # prints "Each person pays 4.0 dollars."
  assert(split_bill(55, 4) == None)  # prints "Each person pays 16.5 dollars."
  assert(split_bill(0, 9) == None)   # prints "Each person pays 0.0 dollars."
  assert(split_bill(73, 5) == None)  # prints "Each person pays 17.52 dollars."
  assert(split_bill(109, 8) == None) # prints "Each person pays 16.35 dollars."
  print("... done!")

  """Question 4: circles_intersect"""
def circles_intersect(x1, y1, r1, x2, y2, r2):
  distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
  if distance <= (r1 + r2):
    return True
  else:
    return False

 
"""Testing Question 4 implementation"""  
def test_circles_intersect():
  print("Testing circles_intersect()...", end="")
  assert(circles_intersect(0, 0, 2, 3, 0, 2) == True)
  assert(circles_intersect(0, 0, 2, 4, 0, 2) == True)
  assert(circles_intersect(0, 0, 2, 5, 0, 2) == False)
  assert(circles_intersect(3, 3, 3, 3, -3, 3) == True)
  assert(circles_intersect(3, 3, 3, 3,- 3, 2.99) == False)
  print("... done!")

"""Question 5: valid_RGB"""
def valid_RGB(red=0,green=0,blue=0): # fill in the parameters!
  if (float(red) >=0 and float(red) <= 255) and (float(green) >=0 and float(green) <= 255) and (float(blue) >=0 and float(blue) <= 255):
    return True
  else:
    return False


"""Testing Question 5 implementation"""  
def test_valid_RGB():
  print("Testing valid_RGB()...", end="")
  assert(valid_RGB() == True)
  assert(valid_RGB(150, 200, 15) == True)
  assert(valid_RGB(100, 300, 100) == False)
  assert(valid_RGB(green=255) == True)
  assert(valid_RGB(red=0, green=45) == True)
  assert(valid_RGB(red=256) == False)
  print("... done!")

"""Question 6: Fix the Code"""
# Remove the triple quotes from the following block of code to run this!
def buggy_function(x):

  if type(x) == str:
    return False
    
  is_even = (x % 2 == 0)
  
  if type(x) != int: 
    return False

  if x <= 10:
    if is_even:
      return True
    else:
      return False
  elif x > 10:
    if not is_even:
      return True
    else:
      return False
  else:
    return False


def test_buggy_function():
  print("Testing buggy_function()...", end="")
  assert(buggy_function(4) == True)
  assert(buggy_function(10) == True)
  assert(buggy_function(11) == True)
  assert(buggy_function(7) == False)

  assert(buggy_function(0) == True)
  assert(buggy_function(-5) == False)
  assert(buggy_function(-8) == True)
  assert(buggy_function(14) == False)

  assert(buggy_function(13.0) == False)
  assert(buggy_function("uh oh") == False)
  print("...done!")




  
if __name__ == '__main__':
  test_get_grade()
  test_pay_bill()
  test_split_bill()
  test_circles_intersect()
  test_valid_RGB()
  test_buggy_function() 