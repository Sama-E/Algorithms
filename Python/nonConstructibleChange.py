# Given an array of positive integers representing the values
# of coins in your possession, write a function that reurns 
# the minimum amount of change( min sum of money ) that 
# you cannot create. The given coins can have any positive 
# integer value and aren't neccessarily unique.


coins = [5, 7, 1, 1, 2, 3, 22]

def NonConstructibleChange(coins):
  coins.sort()

  currentChangeCreated = 0
  for coin in coins:
    if coin > currentChangeCreated + 1:
        return currentChangeCreated + 1
    currentChangeCreated += coin

  return currentChangeCreated + 1

print(NonConstructibleChange(coins)) 