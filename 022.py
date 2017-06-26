# Names scores
# Problem 22
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a
# name score.
# 
# For example, when the list is sorted into alphabetical order, COLIN, which
# is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
# would obtain a score of 938 × 53 = 49714.
# 
# What is the total of all the name scores in the file?

filename = input('enter source file for names: ')


with open(filename) as source:
    read_lines = sorted(source.readlines())

namescores = []

def scoreString(s):
    """returns int of score of s"""
    total = 0
    newstring = s.upper()
    print(newstring)
    for i in range(len(newstring) - 1):
        print('value of',newstring[i],'is',(int(ord(newstring[i]) - 64)))
        total += (ord(newstring[i]) - 64)
    print(total)
    return total
    
for i in range(len(read_lines)):
    #print(i)
    #print(read_lines[i])
    #print(scoreString(read_lines[i]))
    namescores.append(scoreString(read_lines[i]) * (i + 1))
        


print(sum(namescores))


