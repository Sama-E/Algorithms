# Write a function that, given a string, returns its longest palindromic 
# substring.

# A palindrome is defined as a string that's written the same forward
# and backward. Note that single-character strings are palindromes.

# You can assume taht there will only be one longest palindromic 
# substring.

string = "abaxyzzyxf"
output = "xyzzyx"

string1 = "xyzzyxfaba"
output1 = "xyzzyx"

string2 = "abaxyzzyxfxyzzy"
output2 = "xyzzyx"

string3 = "abc"
output3 = ""

# 1. Check for palindrome = isPalindrome
# 2. Set leftIdx = 0 and rightIdx = len(string) - 1
# 3. While leftIdx < rightIdx
# 4. If leftIdx != to rightIdx
# 5. Return False
# 6. Else: leftIdx +=1, rightIdx -=1
# 7. If iteration complete Return True

# 8. Find longestSubstring and check palindrome
# 9. Iterate through length of string beginning with i = 0
# 10. Iterate through string starting from i to length of string
# 11. Substring = string[i :(to) j+1]
# 12. If substring length is greater than longestSubstring length
# And substring is palidrome (isPalidrome(substring))
# 13. longestSubstring = substring
# 14. After all iterations Return longestSubstring

# O(n^3) Time | O(n) Space
# n = length of string
# 3 = 2 for loops + 1 while loop
def longestPalindromicSubstring(string):
    longestSubstring = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i : j + 1]
            print(substring)
            if len(substring) > len(longestSubstring) and isPalindrome(substring):
                longestSubstring = substring
    return longestSubstring


def isPalindrome(string):
  leftIdx = 0
  rightIdx = len(string) - 1
  while leftIdx < rightIdx:
    if string[leftIdx] != string[rightIdx]:
      return False
    leftIdx += 1
    rightIdx -= 1
  
  return True


print(longestPalindromicSubstring(string))
print(longestPalindromicSubstring(string1))
print(longestPalindromicSubstring(string2))
print(longestPalindromicSubstring(string3))