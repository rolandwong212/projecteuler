#!/bin/python3

import sys

# text input
# First line contains T that denotes the number of test cases. This is followed
# by T lines, each containing an integer, N.

# this line reads a single line from stdin, removes first and last chars,
# casts to type int, assigns value to t
t = int(input().strip())

# these lines use index a0 over t lines and assigns each line to n after casting
# to type int
for a0 in range(t):
    n = int(input().strip())
    
