# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(string):
    """Returns boolean value"""
    # print("input string is", string)
    # string is zero or one char? -- return yes
    if len(string) == 0:
        return True
    elif len(string) == 1:
        return True
    # is first char same as last? -- strip first, last, call isPalindrome on
    # stripped string
    elif string[0] is string[-1]:
        return isPalindrome(string[1:len(string)-1])
    # otherwise return no
    else:
        return False

#isPalindrome(makestring(999*range(999 to 1)))
# for i in range 999 to 1
# if isPalindrome(999*i):
#    print(999*i)


for i in range(999,100,-1):
    for j in range(999,100,-1):
        if isPalindrome(str(i*j)) is True:
            print(i*j,"palindrome: i",i,"j",j)
    #print(i,"is",999*i)
    # print("string version: ",str(999*i))
    #if isPalindrome(str(999*i)) is True:
    #    print(i, "is the factor of a palindrome,", 999*i)


    
