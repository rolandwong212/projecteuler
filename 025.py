# 1000-digit Fibonacci number
# Problem 25
# The Fibonacci sequence is defined by the recurrence relation:
# 
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
# 
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
# 
# What is the index of the first term in the Fibonacci sequence to contain
# 1000 digits?

# sounds like each fib term should be added to a list, then check
# len(str(fib[i])) = 1000

# initialize list of fibonacci terms
fib = [1, 1]

# initialize index at 2nd term
i = 1

while len(str(fib[i])) != 1000:
    fib.append(fib[i] + fib[i - 1])
    i += 1

print(i)
