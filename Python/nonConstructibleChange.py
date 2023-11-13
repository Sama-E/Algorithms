# Given an array of positive integers representing the values
# of coins in your possession, write a function that returns 
# the minimum amount of change( min sum of money ) that 
# you cannot create. The given coins can have any positive 
# integer value and aren't neccessarily unique.


coins = [5, 7, 1, 1, 2, 3, 22]
output = 20

coins0 = [5, 7, 1, 1, 2, 3, 25, 37, 16, 15, 22, 31, 21]
output0 = 187

# O (n logn) Time O(1) Space
def NonConstructibleChange(coins):
  # Sort coins
  coins.sort()

  # Set change = 0
  currentChangeCreated = 0
  # Loop through coins
  for coin in coins:
    # If cooin > change + 1
    if coin > currentChangeCreated + 1:
        # Return change + 1
        return currentChangeCreated + 1
    # Else add coin to change
    currentChangeCreated += coin
  # Return change + 1
  return currentChangeCreated + 1

print(NonConstructibleChange(coins))
print(NonConstructibleChange(coins0))