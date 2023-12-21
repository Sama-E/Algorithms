# Write a function that takes in an array of at least three integers and,
# without sorting the input array, returns a sorted array of the three
# largest integers in the input array.

# The function should return duplicate integers if necessary; for example,
# it should return [10, 10, 12] for aninput array of [10, 5, 9, 10, 12].


array = [141, 1, 17, 1, -17, -27, 18, 541, 8, 7, 7]
output = [18, 141, 541]

array1 = [1, 17, 1, -17, -27, 18, 8, 7, 7]
output1 = [8, 17, 18]

array2 = []
output2 = []

array3 = [1, 17]
output3 = [1, 17]

def findThreeLargestNumbers(array):
    numberElementsInArrayM = 3
    arrayM = numberElementsInArrayM*[-float("inf")]
    for i in array:
        if i < arrayM[0]:
            continue
        
        arrayM[0] = i
        for j in range(numberElementsInArrayM-1):
            if arrayM[j] < arrayM[j+1]:
                break
            arrayM[j], arrayM[j+1] = arrayM[j+1], arrayM[j]

    return arrayM

print(findThreeLargestNumbers(array))
print(findThreeLargestNumbers(array1))
print(findThreeLargestNumbers(array2))
print(findThreeLargestNumbers(array3))