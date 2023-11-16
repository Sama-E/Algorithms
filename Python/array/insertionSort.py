# Write a function that takes in an array of integers and returns
# a sorted version of that array. Use the insertion Sort algorithm 
# to sort array.

array = [8, 5, 2, 9, 5, 6, 3] 
output = [2, 3, 5, 5, 6, 8, 9]

array1 = [8, -5, -2, 9, 5, 6, 3] 
output1 = [ -5, -2, 3, 5, 6, 8, 9]

array2 = [8] 
output2 = [8]

array3 = [1, 2, 3, 4] 
output3 = [1, 2, 3, 4]

# Search for smallest element between 2 indices, 
# then insert smallest element index to the front of array

# 1. Iterate through starting at index 1, index 0 is sorted because
# it is the first element in the array
# 2. Initialize i = index so index doesn't return to the for loop
# 3. While i is greater than 0 and element in array[i] is greater 
# than element in array[i-1] then swap elements
# 4. Decrement i (return to step 3)

# O(n^2) Time | O(1) Space
def insertionSort(array):
    for index in range(1, len(array)):
        i = index
        while i > 0 and array[i] < array[i-1]:
            array[i], array[i-1] = array[i-1], array[i]
            i -= 1
    return array


print(insertionSort(array))
print(insertionSort(array1))
print(insertionSort(array2))
print(insertionSort(array3))