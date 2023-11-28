usernames = "hydra"
output = "YES"

usernames1 = "ace"
output1 = "YES"

def possibleChanges(usernames):
  newArray=[]
  letter = 0
  length = len(usernames) - 1
  for letter in usernames:
    unicodeLetter = ord(letter)
    newArray.insert(length, unicodeLetter)
  
  currentIdx = 0
  while currentIdx < len(newArray) - 1:
    smallestIdx = currentIdx
    for rangeIdx in range(currentIdx+1, len(newArray)):
      if newArray[smallestIdx] > newArray[rangeIdx] and newArray[smallestIdx] != newArray[0]:
        smallestIdx = rangeIdx
        print("YES")
      else:
        print("NO")
    break


print(possibleChanges(usernames))


