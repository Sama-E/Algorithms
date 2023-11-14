# Valid Subsequence

# Given two non-empty arrays of integers, write a function
# that determines whter the second array is a subsequence 
# of the first one.

# A subsequence of an array is a set of numbers that aren't
# necessarily adjacen in the array but that are inthe same 
# order as they appear in the array. For instance, the numbers
# [1,3,4] from a subsequence of the array [1,2,3,4], and so do 
# the numbers [2,4]. Note that a single number in an array and
# the array itself are both valid subsequences of the array.

array = [5, 1, 22, 25, 6, -1, 10]
sequence = [1, 6, -1, 10]
output = "true"

array0 = [5, 1, 22, 25, 6, -1]
sequence0 = [1, 6, -1, 10]
output0 = "false"

array1 = [5, 1, 22, 25]
sequence1 = [1, 6, -1, 10]
output1 = "false"

def isValidSubsequence(array, sequence):
  # Set arrayIndex = 0 and sequenceIndex = 0
  arrIdx = 0
  seqIdx = 0
  # While Iterating through array and sequence
  # as long as the length of array is less than array index 
  # and the length of sequence is less than sequence index
  while arrIdx < len(array) and seqIdx < len(sequence):
    # if arrayIndex[element] == sequenceIndex[element]
    if array[arrIdx] == sequence[seqIdx]:
      # Move to next sequenceIndex
      seqIdx += 1
    # Else move to next arrayIndex
    arrIdx += 1
  # Loop ends once the sequence length is reached
  # if the sequenceIndex == sequence length then all 
  # sequence[index] matched array[index], if not then 
  # sequenceIndex is less than sequence length because 
  # some sequence[index] were not found in array[index]
  # Return boolean(sequenceIndex == sequence length)
  return seqIdx == len(sequence)


print(isValidSubsequence(array, sequence))
print(isValidSubsequence(array0, sequence0))
print(isValidSubsequence(array1, sequence1))