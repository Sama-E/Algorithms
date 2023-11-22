
# Write a function that takes in a non-empty strings and returns a list of 
# characters that are common to all strings in the list, ignoring multiplicity.

# Note that the strings are not guaranteed to only contain alphanumeric 
# charcaters. The list you return can be in any order.

strings = ["abc", "bcd", "cbaccd"]
output = ["b", "c"]

# 1. Set object allChr = {}
# 2. Iterate through strings
# 3. Put elements from strings in a set called allChr
# 4. Iterate through characters in the allChr 
# 5. If character in allChr is not represented in countChr, then
# countChr[element] = 0 else countChr[element] += 1 | countChr holds character: count
# 6. Set new commonChr = []
# 7. Iterate through  object countChr destructure countChr
# 8. If count equal length of strings, then append commonChr(character)
# 9. Return commonChr



def commonCharacters(strings):
    countChr = {}
    for element in strings:
        allChr = set(element)
        for character in allChr:
            if character not in countChr:
                countChr[character] = 0
            countChr[character] += 1
        
    commonChr = []
    for character, count in countChr.items():
        if count == len(strings):
            commonChr.append(character)

    return commonChr



print(commonCharacters(strings))


# def commonCharacters(strings):
#     return set.intersection(*[{char for char in string} for string in strings])


# print(commonCharacters(strings))