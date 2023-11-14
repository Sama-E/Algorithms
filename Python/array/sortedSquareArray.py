# Sorted Square Array

# Write a function that takes in a non-empty array
# of integers that are aorted in ascending order and
# reutrns a new array of the same length with the 
# squares of the original integers also sorted in 
# ascending order.

array = [1, 2, 3, 5, 6, 8, 9]
output = [1, 4, 25, 36, 64, 81]

array0 = [4, 7, 8, 9, 10]
output0 = []

array1 = [5, 4, 1, -2, 3]
output1 = []

# O(n^2) - Iterate through array
# twice - while loop and sort
# def sortedSquaredArray(array):
#     # Initialize newArray
#     newArray = []
#     # Set index = 0
#     i = 0
#     #Iterate through array
#     while i < len(array):
#         # Square arrray element
#         x = array[i]**2
#         # x = pow(array[i], 2)
#         # Append to newArray
#         newArray.append(x)
#         # Next index
#         i += 1
#     # Sort Array
#     newArray.sort()
#     # Return newArray
#     return newArray

# O(n) - Iterate through array once -
# sorting inside for loop
# Pointers
def sortedSquaredArray(array):
    # Initialize newArray
    newArray = [0 for _ in array]
    # Set index = 0
    i = 0
    # Set 2 pointers - small & large
    small = 0
    large = len(array) - 1
    # Iterate through indices in reverse 
    # sequence the length of the array
    for i in reversed(range(len(array))):
        # Initialize pointer elements
        smaller = array[small]
        larger = array[large]

        # If the absolute of the small element
        # is larger than the absolute of large
        # element then square small element
        # otherwise square large element
        if abs(smaller) > abs(larger):
            # Square small element add to 
            # newArray
            newArray[i] = smaller**2
            # Move to next index
            small += 1
        else:
            # Square large element add to 
            # newArray
            newArray[i] = larger**2
            # Move to previous index
            large -=1

    return newArray;


print(sortedSquaredArray(array))
print(sortedSquaredArray(array0))
print(sortedSquaredArray(array1))