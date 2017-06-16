# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first
# ten terms would be:
# 
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# 
# Let us list the factors of the first seven triangle numbers:
# 
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# 
# What is the value of the first triangle number to have over five hundred
# divisors?



def sumIntegers(n):
    """This will return the sum of the natural numbers from 1 to n."""
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum

def factors(n):
    """This returns a list of the factors of n."""
    # q & d, brute force
    list = [1,]
    for i in range(2,n + 1):
        if n % i is 0:
            list.append(i)
    return list

def main(*args):
    """Calls other functions."""
    # instring = input('number: ')
    # print(sumIntegers(int(instring)))
    # print(len(factors(int(instring))))
    i = 1
    while len(factors(i)) < 500:
        print(i,len(factors(i)))
        i += 1
    return 

main()