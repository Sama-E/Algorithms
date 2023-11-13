# Write a function that takes in 2 non-empty arrays in integers, 
# finds the pair of numbers(one from each array) whose absolute 
# difference is closest to zero, and return an array containing 
# these two number, with the number from the first array in the 
# first position.

# Note that the absolute difference of two integers is the 
# distance between them in the real number line. For example, 
# the absolute difference of -5 and 5 is 10, and the absolute 
# difference of -5 and -4 is 1.

# You can assume that there will only be one pair of numbers 
# with the smallest difference.


array1 = [-1, 5, 10, 20, 28, 3]
array2 = [26, 134, 135, 15, 17]
output = [28, 26]

array3 = [-11, 25, 13, 10, 48, 63]
array4 = [6, 34, 35, 5, 37]
output = [10, 6]

array5 = [-15, 52, 0, 23, 18, 33]
array6 = [46, 114]
output = [52, 46]

# float("inf") = returns a floating-point positive infinity
# 1. Sort Arrays
# 2. Initialize index in each array = 0
# 3. Initialze smallestSum and currentSum with floating-point 
# poisitive infiinity. smallestSum stores smallest sum throughout 
# iterations. CurrentSum is sum in each iteration.
# 4. While idx1 < length of array1 and 
# idx2 < length of array2, num1 = array1[idx1] & num2 = array2[idx2]
# 5. If num1 < num2, currentSum = num2 - num1, then next idx1
# 5. Else if num1 > num2, currentSum = num1 - num2, then next idx2
# 6. Else return [num1, num2]
# 7. During each iteration compare smallestSum and currentSum to 
# determine smallest sum closest to zero, if smallestSum > currentSum, 
# then smallestSum = currentSum. output = smallestSum[idx1, idx2]
# output = [num1, num2]

# O(n logn + m lognm) Time | O(1) Space | n = length of arrayOne, 
# m = length arrayTwo
def smallestDifference(array1, array2):
    output = []
    
    array1.sort()
    array2.sort()

    idx1 = 0
    idx2 = 0

    smallestSum = float("inf")
    currentSum = float("inf")

    while idx1 < len(array1) and idx2 < len(array2):
        num1 = array1[idx1]
        num2 = array2[idx2]

        if num1 < num2:
            currentSum = num2 - num1
            idx1 += 1
        elif num1 > num2:
            currentSum = num1 - num2
            idx2 += 1
        else: 
            return [num1, num2]

        if smallestSum > currentSum:
            smallestSum = currentSum
            output = [num1, num2]

    return output


print(smallestDifference(array1, array2))
print(smallestDifference(array3, array4))
print(smallestDifference(array5, array6))