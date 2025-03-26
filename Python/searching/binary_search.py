1 # Note: This is not a complete program.
#
# The binary_search function performs a binary search on a
# String list. The list is searched for the string passed to
# the value parameter. If the string is found, its subscript
# is returned. Otherwise, − 1 is returned indicating the value
# was not found in the list. 

def binary_search(arr, value):
  # Set the initial values.
  first = 0
  last = len(arr)-1
  position = -1
  found = False

  # Search for the value
  while not found and first <= last:
    # Calculate the mid point.
    middle = (first + last)/2

    # If the value is found at the mid point...
    if arr[middle] == value:
      found = True
      position = middle
    # else if value is in the lower half...
    elif arr[middle] > value:
      last = middle-1
      # else if value is in the upper half...
    else:
      first = middle+1

  # Return the position of the item, or -1
  # if it was not found.
  return position