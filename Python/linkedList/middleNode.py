# You are given a Linked List with at least one node. Write a 
# function that returns the middle node of the Linked List. If 
# there are two middle nodes (i.e. an even length list), your 
# function should return the second of these nodes.

# Each LinkedList node has an integer value as well as a next 
# node pointing to the next node in the list or to None/null if 
# it's the tail of the list.

linkedList = [2,7,3,5]
output = [3,5]

# 1. Initialize current node = head oflinkedList(1st node)
# 2. Initialize total = 0
# 3. While current node is not Tail(end of LL = None)
# 4. Add count node, add 1 to total, move to next node 
# currentNode = currentNode.next
# 5. total = Calculated Total
# 6. Initialize middle node = head of linkedList(1st node)
# 7. Iterate list = For index in range of total/2, stop at total/2 
# 8. middle index = middle node 
# 9. if total is even middle node = next node (middlen node.next)
# 10. Return middle node


# O(n) Time | O(1) Space | n: nodes in linked List
def middleNode(linkedList):
    # Find Length
    currentNode = linkedList
    total = 0
    while currentNode != None:
        total += 1
        currentNode = currentNode.next

    # Find Middle Node
    middleNode = linkedList
    for _ in range(total//2):
        middleNode = middleNode.next
    return middleNode


# 1. Initialize runner(slow runner) = head of linked List
# 2. Initialize nextRunner(fast runner) = head of linked List
# 3. While nextRunner is not None and nextRunner pointer is not None
# 4. runner is the runner pointer = next node
# 5. nextRunner is the nextRunner pointer pointer = next next node
# 6. nextRunner is running through list twice as fast so when nextRunner 
# reaches end of list, runner is in the middle of list
# 7. Return runner

# O(n) Time | O(1) Space | n: nodes in linked List
def middleNodeRunner(linkedList):
    runner = linkedList
    nextRunner = linkedList

    while nextRunner != None and nextRunner.next != None:
        runner = runner.next
        nextRunner = nextRunner.next.next
    return runner