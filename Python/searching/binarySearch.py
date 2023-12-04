# Write a function that takes in a sorted array of integers as well as a
# target integer. The function should use the Binary Search algorithm
# to determine if the target integer is contained in the array and should
# return its index if its is otherwise -1.


array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33

array1 = [2, 8, 13, 52, 64, 73]
target1 = 0

array2 = [20, 31, 32, 43, 55, 65, 71, 74, 78, 83]
target2 = 71


def binarySearch(array, target):
  left = 0
  right = len(array) - 1
  while left <= right:
      mid = (left + right) // 2
      if target < array[mid]:
          right = mid - 1
      elif target > array[mid]:
          left = mid + 1
      elif array[mid] == target:
          return mid

  return -1


# ----------------------------------------------------------------------

def binary_SearchHighLow(array, target):
    return binary_Search(array, target, 0, len(array) - 1)

def binary_Search(array, target, low, high):
  if low > high:
    return -1
  else:
    mid = (low + high)//2
    if array[mid] == target:
      return mid
    elif array[mid] < target:
      return binary_Search(array, target,mid + 1, high)
    else:
      return binary_Search(array, target, low, mid - 1)
    

# ---------------------------------------------------------------


print(binarySearch(array, target))
print(binarySearch(array1, target1))
print(binarySearch(array2, target2))

print(binary_SearchHighLow(array, target))
print(binary_SearchHighLow(array1, target1))
print(binary_SearchHighLow(array2, target2))