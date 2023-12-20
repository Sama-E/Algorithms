# Write a function that takes in a string made up 
# of brackets ( (, [, {, }, ], ) ) and other 
# optional characters. The function should return
# a boolean representing whether the string is 
# balanced with regards to brackets.

# A string is said to be balanced if it has as 
# many opening brackets of a certain type as it 
# has closing brackets of that type and if no brackets
# that comes before it, and similarly, a closing
# brackets can't overlap each other as in [()].

string = " ([])(){}(())()() "
output = True

string1 = " ([])(){}(()() "
output1 = False

string2 = " "
output2 = True

# 1. Set dictionary of pairs for opposite elements in the string.
# 2. Set stack = []
# 3. Loop through string
# 4. If element is not in '(){}[]'
# 5. Else if element is not the stack OR if element is not equal 
# the first/top element in stack, append stack with element
# 6. Else pop stack's first/top element
# 7. Outside loop: Boolean: len(stack) == 0 True | != 0 False


def balancedBrackets(string):
    pairs = { '(' : ')', '[' : ']', '{' : '}' }
    stack = []

    for x in string:
        if x not in '({[]})':
            continue
        elif not stack or pairs.get(stack[-1]) != x:
            stack.append(x)
        else:
            stack.pop()

    return len(stack) == 0


print(balancedBrackets(string))
print(balancedBrackets(string1))
print(balancedBrackets(string2))