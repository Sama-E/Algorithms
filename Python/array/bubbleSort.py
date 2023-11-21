# Write a function that takes in an array of integers and returns a 
# sorted version of that array. Use the Bubble Sort algorithm to sort 
# the array. 

array = [8, 5, 2, 9, 5, 6, 3]
output = [2, 3, 5, 5, 6, 8, 9]

array1 = [1]
output1 = [1]

array2 = [1, 2, 3]
output2 = [1, 2, 3]

array3 = [-4, 5, -1, 3, 6, 7, -10, 10]
output3 = [-10, -4, -1, 3, 5, 6, 7, 10]

# Search for smallest element between 2 indices,
# then swap indices move through array. Check if array is sorted.

# 1. Set isSorted = False (check if array is sorted)
# 2. While array isSorted is False
# 3. isSorted is true if pair of indexed elements are sorted
# 4. Iterate through index of array 
# 5. If element in index is greater than element in next index
# 6. Swap elements
# 7. isSorted remains false if elements are swapped then return to step 4

# O(n) Time | O(1) Space n = length of array / O(n^2) Average & Worst
#  Time | O(1) Space 
def bubbleSort(array):
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(array)-1):
            j = i + 1
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                isSorted = False
    return array

    
# Swap array[i], array[j]
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

print(bubbleSort(array))
print(bubbleSort(array1))
print(bubbleSort(array2))
print(bubbleSort(array3))