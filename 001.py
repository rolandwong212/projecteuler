# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# init array of numbers that are divis by 3 or 5
divisible_by_3_or_5 = []

# init the counter
i = 1

#
# while i < 1000
# if counter (divisble by 3) | (divisible by 5)
# then append to array
#
# i++
#

while i < 1000:
    if (i % 3 is 0) | (i % 5 is 0):
        divisible_by_3_or_5.append(i)

    i+=1
    

print (sum(divisible_by_3_or_5))


