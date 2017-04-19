# https://projecteuler.net/problem=3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#

import math

instring = input('enter number: ')

n = int(instring)

def sieveEratosthenes(n):
# sieveEratosthenes will return a list of primes less than n
    list = [("true") for x in range(n)]
    for i in range(2,int(math.sqrt(n))):
        if list[i] is "true":
            for j in range(i*i,n,i):
                list[j] = "false"
    return list



primes = sieveEratosthenes(n)

print("here are the primes up to", n)

for i in range(n):
    if primes[i] is "true":
        print(i)

#  grtstPrmDvsr will return the largest prime that is a divisor of n
def grtstPrmDvsr(n):
    pass


