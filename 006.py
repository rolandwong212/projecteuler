# Sum square difference
# Problem 6
# The sum of the squares of the first ten natural numbers is,
# 
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

# lambda x: x ** 2


def sumOfSquares(terms):
    """Returns sum of squares of each term."""
    value = 0
    for i in terms:
        value = value + i * i
    return value

def squareOfSums(terms):
    """Returns square of the all the terms added together."""
    sum = 0
    for i in terms:
        sum = sum + i
    return sum * sum

def main(*args):
    """This function calls the other functions."""
    # enter lower bound instring = input('enter number: ')
    lowerbound = input('enter lowerbound: ')
    upperbound = input('enter upperbound: ')
    # enter upper bound
    # create range from lower to upper+1
    # print absolute value of sumOfSquares(inrange) - squareOfSums(inrange)
    print(abs(sumOfSquares(range(int(lowerbound),int(upperbound) + 1)) - \
              squareOfSums(range(int(lowerbound),int(upperbound) + 1))))
    pass

main()
