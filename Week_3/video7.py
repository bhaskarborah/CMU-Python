# Solutions:
# 1. 
def my_print(s, num):
    for i in range(num):
       print(s)

# 2.
def all_evens(s):
    for i in range(len(s)):
        if i%2 == 0:
            print(s[i])

# 3. 
for i in range(1, 101):
    if i % 6 == 0:
       print(i)