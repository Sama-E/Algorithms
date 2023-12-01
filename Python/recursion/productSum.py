# Write a function that takes in a "special" array and returns its product sum.

# A "special" array is a non-empty array that contains either integers or other 
# "special" arrays. The product sum of a "special" array is the sum of its elements,
# where "special" arrays inside it are summed themselves and then multiplied by
# their level of depth.

# The depth of a "special" array is how far nested it is. For instance, the depth
# of the [] is 1; the depth ofthe inner array in [[]] is 2; the depth of the 
# innermost array is [[[]]] is 3.

# Therefore, the product sum of:
# [x,y] = x + y 
# [x,[y,z]] = x + 2*(y+z)
# [x,[y,[z]]] = x +2*(y + (3*z))

array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
output = 5 + 2 + 2*(7+(-1)) + 3 + 2*(6 + 3 * ((-13 + 8) + 4))
output = 12

array1 = [6, [5, 2], -2, [7, -1, [3, 9]], [6], [-13, 8]]
output1 = 104


array2 = [[[3, 9]],[[6, 4]], [[-13, 8]]]
output2 = 102

# 1. Set multiplier=1 in parameter(argument) of function productSum()
# 2. Set sum = 0
# 2. Iterate through array
# 3. If array[i] type is list | type()
# 4. Add to sum recursion of productSum() passing array[i], and
# multiplier + 1
# 5. Else sum += i
# 6. After iteration return sum * multiplier

# O(n) Time | O(m)
# n = number of elements in array
# m = deepest depth(multiplier) of "special" arrays in the array 
def productSum(array, multiplier=1):
    sum = 0
    for i in array:
        if type(i) is list:
            sum += productSum(i, multiplier + 1)
        else:
            sum += i
    return sum * multiplier



def productSum1(array, multiplier=1):
    return multiplier * sum(
        productSum(i, multiplier+1) 
        if isinstance(i, list) 
        else i 
        for i in array
    )




print(productSum(array))
print(productSum(array1))
print(productSum(array2))

print(productSum1(array))
print(productSum1(array1))
print(productSum1(array2))