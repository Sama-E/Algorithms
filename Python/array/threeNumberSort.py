# You're given an array of integers and another array of 3
# distinct integers. The first array is guaranteed to only 
# contain integers that are in the second array, and the 
# second array represents a desired order for the integers 
# in the array. For example, a second array of [x,y,z] 
# represents a desired order of [x, x, ..., y, y, ..., z, z]
# in the first array. 

# Write a dunction that sorts the first array according to 
# the desired order in the second array.

# The function should perform this in place (i.e., it should 
# mutate the input array), and it shouldn't use any auxiliary
# space (i.e., it should run with constant space: 0(1) space).

# Note that the desired order won't necessarilty be ascending
# or descending and that the first array won't necessarily
# contain all three integers found in the second array - it 
# might only contain one or two.



array = [1, 0, -1, 0, 1, -1, 0, 1, 1]
order = [0, 1, -1]
output = [0, 0, 0, 1, 1, 1, -1, -1]

def threeNumberSort(array, order):
  orderCounts = [0, 0, 0]

  # From elements in order, count number of each element
  # in the array 
  for i in array:
    orderIdx = order.index(i)
    orderCounts[orderIdx] += 1

  # 
  for j in range(len(order)):
    x = order[j]
    count = orderCounts[j]

    numElementsBefore = sum(orderCounts[:j])

    for k in range(count):
      currentIdx = numElementsBefore + k
      array[currentIdx] = x

  return array


print(threeNumberSort(array, order))