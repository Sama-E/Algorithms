# The Factorial sequence is defined as follows: the first number of the sequence
# is 0, the second is 1, and the nth number is the product of the (n)th and (n-1)th 
# numbers. Write a function that takes in an integer n and returns the nth Factorial
# number.

n = 3 
output = 6

n1 = 6.8
output1 = 720

n2 = 0
output2 = 1


# O(n^1) Time | Space O(n) 
# n = recursion((sum-1))

# 1. If n = 0, return 1 (1, 1, 2, 6, 24, 120 ...)
# 2. Else if n = 1, return n
# 3. Else return using recursion = n * getNthFact(n-1)

import math

def getNthFact(n):
    floorN = math.floor(n)

    if floorN == 0:
        return 1
    elif floorN == 1:
        return floorN
    elif floorN > 1 :
        return floorN * getNthFact(floorN-1)
    

print(getNthFact(n))
print(getNthFact(n1))
print(getNthFact(n2))