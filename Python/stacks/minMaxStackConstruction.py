# Write MinMaxStack class for a Min Max Stack. The class should
# support:
#  - Pushing and popping values on and off the Stack
#  - Peking at the value at the top of the Stack
#  - Getting both the minimum and the maximum values in
# the stack at any given point in time.

# All class methods, when considered independently,
# should run in constant time and with constant space.







# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        newMinMax = { "min": number, "max": number }
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max"], number)
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)
        
    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["min"]

    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["max"]

    def printStack(self):
        print(self.stack)


myList = MinMaxStack()
myList.push(5)
myList.push(6)
myList.push(7)
myList.push(8)
myList.push(9)
myList.printStack()
print(myList.getMax())
print(myList.getMin())
print(myList.peek())
myList.pop()
print(myList.peek())
myList.printStack()