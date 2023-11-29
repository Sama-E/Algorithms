# Write a function that takes in a non-empty string and that returns a boolean
# representing whether the string is a palindrome.

# A palindrome is defined as a string that's written the same forward and backward.
# Note that single-character strings are palindromes.

string = "abcdcba"
output = True

string1 = "a"
output2 = True

string2 = "This is not"
output2 = False


# 1. Set isPalindrome = True
# 2. Set 2 pointers right and left starting at the end
# 3. Iterate through string from left at the beginning of string
# 4. Iterate through string from right at the end of the string
# 5. If string[left] == string[right], set isPalindrome = True,
# move to next left and right
# 6. Else isPalindrome = False
# 7. Return isPalindrome

def isPalindrome(string):
  isPalindrome = True
  left = 0
  right = len(string)
  for left in range(len(string)):
    for right in reversed(range(len(string))):
      if string[left] == string[right]:
        isPalindrome = True
        left += 1
        right -= 1
      else:
        isPalindrome = False
        return isPalindrome
    return isPalindrome


    



def isPalindrome1(string):
  leftIdx = 0
  rightIdx = len(string) - 1
  while leftIdx < rightIdx:
    if string[leftIdx] != string[rightIdx]:
      return False
    leftIdx += 1
    rightIdx -= 1
  
  return True

print(isPalindrome(string))
print(isPalindrome(string1))
print(isPalindrome(string2))

print(isPalindrome1(string))
print(isPalindrome1(string1))
print(isPalindrome1(string2))