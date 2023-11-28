# Write a function that takes in a list of unique strings and returns a list 
# of semordnilap pairs. A semordnilap pair is defined as a set of different 
# strings where the reverse of one word is the same as the forward version of 
# the other. For example the words "diaper" adn "repaid" are a semordnilap
# pair, as are the words "palindromes" and "semordnilap".

# The order of the returned pairs and the order of the strings within each 
# pair does not matter.

words = ["diaper", "abc", "test", "cba", "repaid"]
output = [["diaper", "repaid"], ["abc", "cba"]]

# 1. Initialize wordSet  = set(words)
# 2. Initialize reversedPair = []
# 3. Iterate through words 
# 4. Initialize reversed word: reverse = word[::-1]
# 5. If reverse is in wordSet and not in word
# 6. Append reversedPair with word + reverse and
# 7. Remove reverse and word from wordSet
# 8. Return reversedPairs


# O(n * m) Time | O(n * m) Space
# n = number of words
# m = length of word(longest)
def semordnilap(words):
    wordSet = set(words)
    reversedPairs = []

    for word in words:
        reverse = word[::-1]
        if reverse in wordSet and reverse != word:
            reversedPairs.append([word, reverse])
            wordSet.remove(word)
            wordSet.remove(reverse)

        
    return reversedPairs


# 1. Initialize wordDict  = {}
# 2. Initialize reversedPair = []
# 3. Iterate through words
# 4. If word is in wordDict
# 5. Append reversedPair with [word, word(reversed word 
# already set in wordDict)]
# 6. Else reverse the word = word and add to wordDict
# wordDict key: reversedWord, value: word
# 7. Step 4
# 8. Return reversedPairs

# O(n * m) Time | O(n * m) Space
# n = number of words
# m = length of word(longest)
def semordnilap1(words):
    wordDict = {}
    reversedPairs = []

    for word in words:
        if word in wordDict:
            reversedPairs.append([wordDict[word], word])
        else:
            wordDict[word[::-1]] = word

    return reversedPairs



print("1st Function: " )
print(semordnilap(words))
print("")
print("2nd Function: " )
print(semordnilap1(words))