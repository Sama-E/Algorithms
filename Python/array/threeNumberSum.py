# Write a function that takes in a non-empty array distinct integers and an
# integer representing a target sum. The function should find all triplets 
# in the array that sum up to the target sum and return a two-dimensional 
# array of all these triplets. The numbers in each triplet should be ordered 
# in ascending order with repsect to the numbers they hold.
# 
# If three numbers sum up to the the target sum, the function should return 
# an empty array.


array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

output = [
    [-8, 2, 6],
    [-8, 3, 5],
    [-6, 1, 5]
]


# Pointers
# 1. Sort array
# 2. Initialize newArray
# 3. Loop through index of array(length of array - 2 indices)
# 4. 2 Indices(pointers) are left and right
# 5. Initialize left = index + 1
# 6. Initialize right = length of array - 1
# 7. While left < right
# 8. Check currentSum = array[i] + array[left] + array[right]
# 9. If currentSum == targetSum add [array[i] + array[left] + array[right]]
# to newArray then left+=1 and right-=1
# 10. Elif currentSum < targetSum, left +=1
# 11. Elif currentSum > targetSum, right -=1

# O(n^2) Time = for loop + while loop| O(n) Space = newArray length of array 
def threeNumberSum(array, targetSum):
    array.sort()
    newArray = []

    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1

        while left < right:
            currentSum = array[i] + array[left] + array[right]

            if currentSum == targetSum:
                newArray.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            
            elif currentSum < targetSum:
                left +=1
            elif currentSum > targetSum:
                right -=1

    return newArray


print(threeNumberSum(array, targetSum))