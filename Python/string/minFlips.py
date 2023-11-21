# Given a string S, the task is to find minimum flips required 
# to convert an initial binary string consisting of only zeroes
#  to S where every flip of a character flips all succeeding 
# characters as well.

# Input: S = “01011” 
# Output: 3 
# Explanation: 
# Initial String – “00000” 
# Flip the 2nd bit – “01111” 
# Flip the 3rd bit – “01000” 
# Flip the 4th bit – “01011” 
# Total Flips = 3
# Input: S = “01001” 
# Output: 3 
# Explanation: 
# Initial String – “00000” 
# Flip the 2nd bit – “01111” 
# Flip the 3rd bit – “01000” 
# Flip the 5th bit – “01001” 
# Total Flips = 3


target = "01100"
output = 2

target1 = "01011"
output1 = 3

# Function to return the count
# of minimum flips required
# O(n) Time | O(1) Space | n = index in for loop 
def minFlips(target):
	curr = '1'
	count = 0
	
	for i in range(len(target)):
		# If curr occurs in the final string
		if (target[i] == curr):
			count += 1
			
			# Switch curr to '0' if '1'
			# or vice-versa
			curr = chr(48 + (ord(curr) + 1) % 2)

		return count

print(minFlips(target))
print(minFlips(target1))