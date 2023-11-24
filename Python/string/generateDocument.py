
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


def generateDocument(characters, document):
    for character in document:
        charactersFreq = countFrequency(character, characters)
        documentFreq = countFrequency(character, document)
        
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



def generateDocument1(characters, document):
    characterCounts = {}

    # Count characters in characters
    for character in characters:
        if character not in characterCounts:
            characterCounts[character] = 0

        characterCounts[character] += 1

    # Count characters in document 
    for character in document:
        if character not in characterCounts or characterCounts[character] == 0:
            return False

        characterCounts[character] -= 1

    return True



# print(generateDocument1(characters, document))
# print(generateDocument1(characters1, document1))


from collections import Counter
def generateDocument2(characters, document):
    # print (Counter(document) - Counter(characters))
    
    return Counter(document) -  Counter(characters) == {}


print(generateDocument2(characters, document))
print(generateDocument2(characters1, document1))