# Factorial digit sum
# Problem 20
# n! means n × (n − 1) × ... × 3 × 2 × 1
# 
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# 
# Find the sum of the digits in the number 100!

import string

def factorial(n):
    """returns n!"""
    if n is 1:
        return n
    else:
        return n * factorial(n - 1)

num = input('find factorial for this number: ')

print(str(factorial(int(num))))

#listofdigits = str(factorial(100)).split()

print(list(str(factorial(int(num)))))

totalofdigits = 0
for i in range(len(str(factorial(int(num))))):
    totalofdigits += int(list(str(factorial(int(num))))[i])
    print(totalofdigits)

#print(sum(listofidigits))
