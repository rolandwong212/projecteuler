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
    elif string[0] == string[-1]:
        isPalindrome(string[1:len(string)-1])
        return True
    # otherwise return no
    else:
        return False

#isPalindrome(makestring(999*range(999 to 1)))
# for i in range 999 to 1
# if isPalindrome(999*i):
#    print(999*i)

