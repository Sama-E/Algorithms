
# You're given a string of available characters and a string representing a 
# document that you need to generate. Write a function that determins if 
# you can generate the document, your function should return true; otherwise, 
# it should return false.

# You're only able to generate the document if the frequency of unique characters
# in the characters string is greater than or equal to the frequency of unique  
# characters in the document string. For example, if you're given characters = 
# "abcabc" and document = "aabbcc" you cannot generate the document because you're
# missing one c.

# The document that you need to create may contain any characters, including special
# chracters, capital letters, numbers, and spaces.

# Note: you can always generate the empty string("").

characters = "Bste! hetsi ksalF P nothy"
document = "Python Flask is the Best!"
output = True

characters1 = "Bste! hetsi ksalF nothy"
document1 = "Python Flask is the Best!"
output = False

# 1. Count frequency of characters in character and document
# 2. Set count frequency to 0
# 3. Iterate through characters in document
# 4. Iterate through characters in characters
# 5. If character of characters = character of document
# 6. Count + 1 to frequency in characterFrequency
# 7. Iterate through characters in document
# 8. If character of document = character of document
# 9. Count + 1 to frequency in documentFrequency 
# . If count in documentFrequency is greater than count in characterFrequency
# . Return False Else return true 


# O(m *(n + m)) Time | O(1) Space 
# n = number of characters in character
# m = length of document
def generateDocument(characters, document):
    for character in document:
        charactersFreq = countFrequency(character, characters)
        documentFreq = countFrequency(character, document)

        # print(charactersFreq)
        # print(documentFreq)

        if documentFreq > charactersFreq:
            return False
    return True 

def countFrequency(character, string):
    freq = 0
    for char in string:
        if char == character:
            freq += 1

    print(freq)
    return freq


# print(generateDocument(characters, document))
# print(generateDocument(characters1, document1))


# O(n + m) Time | O(c) Space
# n = number of characters in character
# m = length of document
# c = number of unique characters found in 2nd for loop
def generateDocument1(characters, document):
    characterCounts = {}

    # Count characters in characters
    # Place key:character + value:count in characterCount
    for character in characters:
        if character not in characterCounts:
            characterCounts[character] = 0

        characterCounts[character] += 1

    # Iterate through characters in document compare to characterCount 
    for character in document:
        # Compare character in document characterCount
        # Or document character not in characterCount
        # Return False else continue
        if character not in characterCounts or characterCounts[character] == 0:
            return False

        characterCounts[character] -= 1

    return True



# print(generateDocument1(characters, document))
# print(generateDocument1(characters1, document1))


from collections import Counter
def generateDocument2(characters, document):
    
    return Counter(document) -  Counter(characters) == {}


print(generateDocument2(characters, document))
print(generateDocument2(characters1, document1))