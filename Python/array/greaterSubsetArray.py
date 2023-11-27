# Return the subset A in increasing order where the sum of subset array A's
# elements is greater than the sum of subset B elements. If more than one
# subset exists, return the one with the maximal sum.

arr = [3, 7, 5, 6, 2]
output = [6, 7]

arr1 = [3, 7, 5, 6, 2, 10, 15, 30]
output1 = [15, 30]

arr2 = [5, 3, 2, 4, 1, 2]
output2 = [4, 5]

arr3 = [1, 1, 1, 1, 1,]
output3 = []

# 1. Set subArrayA = []
# 2. Sort Array
# 3. Append array[len(array)-1] in subArrayA
# 4. Iterate through and calculate sum
# for i in range (0, len(arr)):
# total = total + arr[i]
# 5. If total > 

def subsetA(arr):
  arr.sort()
  subArr = []
  if not len(arr):
    return 0
  elif len(arr) == 1:
    return arr[0]

  subArr.insert(0, arr[len(arr)-1])
  arr.pop()

  for i in reversed(range(0, len(arr))):
    sumArr = sum(arr)
    sumSubArr = sum(subArr)
    if sumArr > sumSubArr:
      subArr.insert(0, arr[i])
      arr.pop()
      i += 1

    return(subArr)



print(subsetA(arr))
print(subsetA(arr1))
print(subsetA(arr2))
print(subsetA(arr3))