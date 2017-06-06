# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.

# What is the 10 001st prime number?

import math

def sieveEratosthenes(n):
    """sieveEratosthenes calculates primes less than n.

    Returns a list of n boolean values; if True, index is a prime number"""
    list = [("True") for x in range(n)]
    for i in range(2,int(math.sqrt(n))):
        if list[i] is "True":
            for j in range(i*i,n,i):
                list[j] = "False"
    return list

def findnth(list,position):
    """This will find the index of the position-th occurence of True"""
    i = -1
    for j in range(position):
        i = list.index("True", i + 1)
    return i

def main(*args):
    """This calls other functions."""
    n = input('this will calculate primes up to this number: ')
    print(sieveEratosthenes(int(n)).count("True"))
    # we find the 100003th prime, to account for primes in index positions 0 and 1
    print(findnth(sieveEratosthenes(int(n)),10003))
    return

main()
