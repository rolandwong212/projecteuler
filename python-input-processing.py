#!/bin/python3

import sys

# begin text input via stdin
# First line contains T that denotes the number of test cases. This is followed
# by T lines, each containing an integer, N.

# this line reads a single line from stdin, removes first and last chars,
# casts to type int, assigns value to t
t = int(input().strip())

# these lines use index i over t lines and assigns each line to n after casting
# to type int
for i in range(t):
    n = int(input().strip())

# end text input via stdin



# begin text input via file
filename = input('enter source file: ')

# these two open "filename", assigns contents to "ciphertext" as a string
with open(filename) as source:
    ciphertext = source.read()
# source.readline() gets a single line from the file
# If you want to read all the lines of a file in a list you can also use
# list(f) or f.readlines()
