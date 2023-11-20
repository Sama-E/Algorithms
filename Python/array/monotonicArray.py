# Write a function  that takes in an arry of integers and 
# returns a boolean representing whether the array is 
# monotonic (array is  varying in such a way that it 
# either never decreases or never increases.)

# An array is said to be monotonic if its elements, from 
# left to right, are entirely non-increasing or enitrely
# non-decreasing.

# non-increasing elements are necessarily exclusively
# decreasing; they simply don't increase. Similarly, 
# non-decreasing elements aren't necessarily exclusively
# increasing; they simply don't decrease.

# Not that empty arrays and arrays of on element are
# monotonic.

array = [-1, -5, -10, -110, -110, -901]
output = True

array1 = [9, 10, 6, 20, 8, 7, 6]
output1 = False

array2 = []
output2 = True

array3 = [1]
output3 = True

array4 = [1, 2, 3, 4, 5]
output4 = True

# 1. Set increasing and decreasing to true
# 2. Iterate forward through array
# 3. Check if array[i] is less than array[i+1] is true, increasing is true
# 4. Check if array[i] is greater than array[i+1] is true, decreasing is true
# 5. If not, change increasing or decreasing to false.
# 6. Check status of increasing or decreasing during each iteration
# 7. In the end return increasing or decreasing.

# O(n) Time | O(1) Space / n = length of array
def isMonotonic(array):
  # increasing = true
  increasing = True
  # deceasing = true
  decreasing = True
  for i in range(len(array)-1):
    # Check: increasing is true and array[i] is less 
    # or equal to array[i+1]  
    increasing = increasing and array[i] <= array[i+1]
    # Check: decreasing is true and array[i] is greater 
    # or equal to array[i+1] 
    decreasing = decreasing and array[i] >= array[i+1]
  # Return increasing or decreasing
  return increasing or decreasing



print(isMonotonic(array))
print(isMonotonic(array1))
print(isMonotonic(array2))
print(isMonotonic(array3))
print(isMonotonic(array4))