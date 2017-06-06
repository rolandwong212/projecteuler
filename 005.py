# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

# what is the lowest common multiple of all the integers from 1 to n

def gcd(a, b):
    """Greatest common divisor, by Kirby Urner http://4dsolutions.net"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Lowest common multiple, by Kirby Urner http://4dsolutions.net
    
    modified to explicitly use floor division
    """
    return (a * b) // gcd(a, b)


def lcmm(terms):
    """Find the lowest common multiple of the list passed in
    
    by Kirby Urner http://4dsolutions.net
    """
    result = 1
    for i in terms:
        result = lcm(result, i)
    return result


def main(*args):
    """
    Main function; calls other functions.
    """
    print("This will calculate the lowest common multiple of the range specified")
    rangestart = input('enter lower bound (inclusive): ')
    rangeend = input('enter upper bound (inclusive): ')
    print(lcmm(range(int(rangestart),int(rangeend) + 1)))
    return

main()
