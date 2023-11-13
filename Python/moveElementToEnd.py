# You' are given an array of integers and an integer. Write an 
# function that moves all instances of thaat integer in the 
# array to the end of the array and returns the array.

# The function should perform this in place (i.e it should 
# mutate the input array) and doesn't need to maintain the order 
# of the order of the other integers.

array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
output = [1, 3, 4, 2, 2, 2, 2, 2]

array1 = []
toMove1 = 3
output1 = []

array2 = [1, 2, 4, 5, 6]
toMove2 = 3
output2 = [1, 2, 4, 5, 6]

array3 = [5, 1, 2, 5, 5, 3, 4, 6, 7, 5, 8, 9, 10, 11, 5, 5, 12]
toMove3 = 5

# Swapping
# 1. Initialize pointers: left=0, right=len(array)-1
# 2. Iterate through array: while left < right
# 3. Iterate through array and check if last element array[right] == toMove
# 4. If array[right] == toMove, move to previous element: right -= 1
# 5. If array[left] == toMove, then swap array[left], array[right] and 
# move to next element: left += 1
# 6. Return array

# O(n) Time Loop through n times| O(1) Space: swapping in array
def moveElementToEnd(array, toMove):
    left = 0
    right = len(array) - 1
    while left < right:
        while left < right and array[right] == toMove:
            right -= 1
        if array[left] == toMove:
            array[left], array[right] = array[right], array[left]
        left += 1
        return array
        


print(moveElementToEnd(array, toMove))
print(moveElementToEnd(array1, toMove1))
print(moveElementToEnd(array2, toMove2))
print(moveElementToEnd(array3, toMove3))
