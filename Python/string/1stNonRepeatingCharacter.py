# Write a function that takes in a string of lowercase
# English-alphabet letters and returns the index of the 
# string's first non-repeating charcter.

# The first non-repeating character is the first character
# in a string that occurs only once.

# If the input string doesn't have any non-repeating 
# characters, your function should return -1.

string = "afcdcdab"
output = 1
# 'f' is the first non-repeating character

string1 = "asdfghjka"
output1 = 0

string2 = "iuytrewhh"
output2 = 7

string3 = "iuytrew"
output3 = 7

# 1. Set object countCharcter = {}
# 2. Iterate through string and add character/count of character 
# to countCharacter
# 3. Looking for index in string: Iterate through string, 
# 4. Set character = string[idx]
# 5. Look for first character in countCharacter to equal 1
# If countCharacter[charcter] == 1
# 6. Return idx


# def firstNonRepeatingCharacter(string):
#     countCharacter = {}
    
#     for character in string:
#     	countCharacter[character] = countCharacter.get(character, 0) + 1

# 	for idx in range(len(string)):
# 		character = string[idx]
# 		if countCharacter[character] == 1:
# 			return idx
		
# 	return -1

# print(firstNonRepeatingCharacter(string))
# print(firstNonRepeatingCharacter(string1))
# print(firstNonRepeatingCharacter(string2))
# print(firstNonRepeatingCharacter(string3))


# O(n) Time | O(1) Space | n = length of string
from collections import Counter

def firstNonRepeatingCharacter1(string):
  
	countCharacter = Counter(string)
	for idx in range(len(string)):
		character = string[idx]
		if countCharacter[character] == 1:
			return idx

	return -1

print(firstNonRepeatingCharacter1(string))
print(firstNonRepeatingCharacter1(string1))
print(firstNonRepeatingCharacter1(string2))
print(firstNonRepeatingCharacter1(string3))