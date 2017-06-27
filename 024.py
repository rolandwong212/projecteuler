# Lattice paths
# Problem 15
# Starting in the top left corner of a 2×2 grid, and only being able to move
# to the right and down, there are exactly 6 routes to the bottom right corner.
# 
# 
# How many such routes are there through a 20×20 grid?

# as indicated in the title, it's a lattice path problem
# represent the possible paths of length 2n from one corner of an n-by-n grid
# to the opposite corner. The number of paths are the central binomial
# coefficients
# or
# ((2n)!) / ((n!) ** 2)



def factorial(n):
    """returns n!"""
    if n is 1:
        return n
    else:
        return n * factorial(n - 1)

def calcCentralBinomialCoeff(n):
    """given an int n, returns ((2n)!) / ((n!) ** 2)"""
    return factorial(2 * n) // (factorial(n) ** 2)

grid = input('enter n: ')

print(calcCentralBinomialCoeff(int(grid)))


