# Write a function that takes in an array of integers and returns a 
# sorted version of that array. Use selection sort algorithm to sort 
# the array.

array = [8, 5, 2, 9, 5, 6, 3]
output = [2, 3, 5, 5, 6, 8, 9]

array1 = [1]
output1 = [1]

array2 = [1, 2, 3]
output2 = [1, 2, 3]

array3 = [-4, 5, -1, 3, 6, 7, -10, 10]
output3 = [-10, -4, -1, 3, 5, 6, 7, 10]

# Search for smallest element in array, then move smallest 
# element front of array

# 1. Set current index i = 0
# 2. While current index is less than the length of array
# 3. Set smallest element index = current index
# 4. For index in range of current index to length of array, 
# find smaller element index than current index
# 5. If smallest element index is greater than index in the 
# current index range, set smallest index to index in the 
# current index range.
# 6. Swap current index range element with smallest index 
# element in array, then increment current index + 1
# 7. Exit while loop once array is sorted 


def selectionSort(array):
    currentIdx = 0
    while currentIdx < len(array) - 1:
        smallestIdx = currentIdx
        for rangeIdx in range(currentIdx+1, len(array)):
            if array[smallestIdx] > array[rangeIdx]:
                smallestIdx = rangeIdx
        array[currentIdx], array[smallestIdx] = array[smallestIdx], array[currentIdx]
        currentIdx += 1
    return array


print(selectionSort(array))
print(selectionSort(array1))
print(selectionSort(array2))
print(selectionSort(array3))