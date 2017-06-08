# The four adjacent digits in the 1000-digit number that have the greatest
# product are 9 × 9 × 8 × 9 = 5832.

# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450

# Find the thirteen adjacent digits in the 1000-digit number that have the
# greatest product. What is the value of this product?

# make a list of these 1000 digits
# for each occurrence of 0,
# find index, invalidate region index - 12 to index + 12 by putting in list
# named "dontuse"
# for each occurrence of 1,
# find index, make list of region index - 12 to index + 12 by putting in list
# name "2ndchoice"
# are there

# no

# problemspace is 1000 digit list
# create list of tuples (indexstart, product)
# for index, value in enumerate(problemspace)
# create list named index
# while len(i) < 13
# if problemspace[i] != 0:
#     i[x] = problemspace[i]
# else:
#     break
# to start a new list i after the 0

# no

def calcProduct(inlist):
    """Returns product of the 13 terms given.

    Does not modify inlist nor index.
    """
    product = 1
    # does inlist have a zero?
    if "0" in inlist:
        # if yes, return 0
        return 0
    # otherwise return lambda product : product * inlist(range(index))
    else:
        print("here are terms to be multiplied:")
        for x in inlist:
            print(x)
            product *= int(x)
        return product

def main(args):
    """Calls the other functions.

    """
    outlist = []
    # don't call calcProduct on a list shorter than 13 elements
    print("here's the range", range(len(args) - 13))
    for i in range(len(args) - 13):
        # call calcProduct(inputlist(i:i + 12) ie on a slice of inputlist
        outlist.append(calcProduct(args[i:i + 13]))
        # append to outlist
    print(max(outlist))
    print("and here is outlist:")
    print(outlist)
    print("and here is outlist, sorted")
    outlist.sort()
    print(outlist)
    return
    



inlist = input('enter string: ')


main(inlist)
