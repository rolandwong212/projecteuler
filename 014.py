# Longest Collatz sequence
# Problem 14
# The following iterative sequence is defined for the set of positive integers:
# 
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains
# 10 terms. Although it has not been proved yet (Collatz Problem), it is thought
# that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.


def CollatzTerm(n):
    """Returns a Collatz term for n."""
    if n % 2 is 0:
        return n // 2
    else:
        return (3 * n) + 1


def generateCollatzSequence(term):
    """returns list of collatz terms."""
    sequence = [term, ]
    next = term
    # now generate list
    while next > 1:
        sequence.append(CollatzTerm(next))
        next = CollatzTerm(next)
    return sequence

def main(*args):
    """Calls other functions."""
    instring = input('enter first term to compute Collatz sequence: ')
    print(generateCollatzSequence(int(instring)))
    # init list of tuples: starting term, len of collatz seq
    lot = [0, ]
    for i in range(1,100000000):
        lot.append(len(generateCollatzSequence(i)))
    max_value = max(lot)
    return lot.index(max_value)


main()
