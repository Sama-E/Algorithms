# Write a function that takes in an array of unique integers andreturns an array 
# of all permutations of those integers in no particular order. If the inputarray 
# is empty, the function should return an empty array.


array = [1, 2, 3]
output = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


def getPermutations(array):
    permutations = []
    permutationsHelper(array, [], permutations)
    return permutations


def permutationsHelper(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1:]
            newPermutation = currentPermutation + [array[i]]
            permutationsHelper(newArray, newPermutation, permutations)




# No helper needed
def getPermutations2(array):
    result = []
    
    if len(array) == 1:
        return [array]
    
    else:
        for i in range(len(array)):
            for element in getPermutations(array[:i] + array[i+1:]):
                result.append([array[i]] + element)

    return result 

print(getPermutations(array))