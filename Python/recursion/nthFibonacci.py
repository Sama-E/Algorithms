# The Fibonacci sequence is defined as follows: the first number of the sequence
# is 0, the second is 1, and the nth number is the sum of the (n-1)th and (n-2)th 
# numbers. Write a function that takes in an integer n and returns the nth Fibonacci
# number.

# Important note: the Fibonacci sequence is often defined with its first two numbers
# as F0 = 0 and F1 = 1. For the purpose of this question, the first Fibonacci number
# is F0; therefore, getNthFib(1) is equal to F0, getNthFib(2) is equal to F1, etc.

n = 2 
output = 1

n1 = 6
output1 = 5

# Purpose of this question start n = 1 output = 0,
# Instead of n = 0, output = 0
# n = nth position
# 1. If n = 2, return 1 (0, 1, 1, 2 ...)
# 2. Else if n = 1, return 0
# 3. Else return recursion getNthFib(n-1) + getNthFib(n-2)

# O(n^2) Time | Space O(n) 
# n^2 = recursion((n-1), (n-2))
def getNthFib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib(n-1) + getNthFib(n-2)


# Non-recursion
# O(n) Time | Space O(n)
def getNthFib1(n):
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a+b
    return a



# Purpose of this question start n = 1 output = 1,
# And n = 0, output = 0
# n = nth position
# 1. If n = 0, return 0 (0, 1, 1, 2 ...)
# 2. Else if n = 1, return 1
# 3. Else return recursion getNthFib2(n-1) + getNthFib2(n-2)

# O(n^2) Time | Space O(n) 
# n^2 = recursion((n-1), (n-2))
def getNthFib2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return getNthFib2(n-1) + getNthFib2(n-2)




print(getNthFib(n))
print(getNthFib(n1))

print(getNthFib1(n))
print(getNthFib1(n1))

print(getNthFib2(n))
print(getNthFib2(n1))