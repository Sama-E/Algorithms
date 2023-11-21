# Given a non-empty string of lowercase letters and a non-negative integer
# representing a key, write a function that returns a new string obtained
# by shifting every letter in the input string by k positions in the 
# alphabet, where k is the key.

# Note that letter should wrap around the alphabet; in other words, the 
# letter z shifted by one returns the letter a.


string = "xyz"
key = 2
output = "zab"

string1 = "xyz"
key1 = 4
output = "bcd"

string2 = "z"
key2 = 10
output = "k"

# 1. Set new array for new string: newArray = []
# 2. Set new key for new string: newKey = k % 26
# 3. Iterate through string
# 4. For each letter: ord() = returns the unicode integer that 
# represents the character
# 5. For each key: key % 26 = returns the modulus(abs) of the key 
# up to 26 after 26 returning to 1
# 6. Add each letter from string to key to get new letter: 
# newLetter = ord(letter) + key % 26
# ord(a) = 97 & ord(z) = 122 | 
# 7. Change and return newLetter unicode integer to character chr(newLetter):
# if newLetter is <= 122(z)
# else newLetter % 122 + 96
# 8. Append newArray with new letters



def caesarCipherEncryptor(string, key):
  newArray = []
  newKey = key % 26

  for letter in string:
    newLetter = ord(letter) + newKey
    if newLetter <= 122:
      newArray.append(chr(newLetter))
    else:
      newArray.append(chr(newLetter % 122 + 96))

  return "".join(newArray)


print(caesarCipherEncryptor(string, key))
print(caesarCipherEncryptor(string1, key1))
print(caesarCipherEncryptor(string2, key2))