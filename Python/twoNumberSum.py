array0 = [3,5,-4,8,11,1,-1,6]
targetSum0 = 10

array1 = [4,6]
targetSum1 = 10

array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
targetSum2 = 18

array3 = [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47]
targetSum3 = 164

array4 = [15]
targetSum4 = 15

# def twoNumberSum(array, targetSum):
#   for i in range(len(array)-1):
#     firstNum = array[i]
#     for j in range(i + 1, len(array)):
#       secondNum = array[j]
#       if firstNum + secondNum ==targetSum:
#         return [firstNum, secondNum]
#   return []

def twoNumberSum(array, targetSum):
    # Sort Array
    array.sort()
    # Set left index = 0 
    left = 0
    # Set right index = 0
    right = len(array) - 1

    # while right is greater than left
    while left < right:
        # currentSum = left element + right element
        currentSum = array[left] + array[right]
        # if currentSum = targetSum
        if currentSum == targetSum:
            # return left element, right element
            return [array[left], array[right]]
        # else if currentSum is less than targetSum, move to next left index 
        elif currentSum < targetSum:
            left += 1
        # else if currentSum is greater than targetSum, move to previous right index
        elif currentSum > targetSum:
            right -= 1
    # return array of left element and right element adding up to targetSum or return array with no elements
    return []



print(twoNumberSum(array0, targetSum0))
print(twoNumberSum(array1, targetSum1))
print(twoNumberSum(array2, targetSum2))
print(twoNumberSum(array3, targetSum3))
print(twoNumberSum(array4, targetSum4))