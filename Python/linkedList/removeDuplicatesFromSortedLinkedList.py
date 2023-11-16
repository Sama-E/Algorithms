# You're given the head of a Singly Linked List whose nodes are 
# in sorted order with respect to their values. Write a function 
# that returns a modified version of the Linked List that doesn't
# contain any nodes with duplicate values. The Linked List should 
# be modified in place(i.e., you shouldn't create a brand new list), 
# and the modified Linked List hould have its nodes sorted with 
# respect to their values.

# Each Linked List node has an integer value as well as a next node 
# pointing to the next node in the list or to Non / null if it's the 
# tail of the list

linkedList = [1, 1, 3, 4, 4, 4, 5, 6, 6]
output = [1, 3, 4, 5, 6]

linkedList1 = [1, 1, 1, 1, 1, 1]
output = [1]

linkedList2 = [2]
output = [2]

linkedList3 = [1, 2, 3, 4, 5, 6, 6, 6, 6]
output = [1, 2, 3, 4, 5, 6]

# 1. Initialize current node as linkedList head
# 2. Traverse forward throught linked List - one node at a time
# 3. While current node(data & pointer) is not None(it's none at end of LL =
# the end/tail)
# 4. The next node = node after current node (current node.next)
# 5. While next node is not None and if next node.data == current node.data 
# (if nodes are duplicate data)
# 6. Then next node = node after next node (next node.next) - 
# This removes node.pointer(which in turn removes the current node) 
# to point to the following node to repeat the while process 
# if current node does not equal the next node break out of while
# 7. Else: node after current node (current node.next) = next node
# 8. Else: currentNode = nextNode


# next = pointer
# value = data
# O(n) Time | O(1) Space | n = number of nodes | 1 = extracted in place
def removeDuplicatesFromSortedLinkedList(linkedList):
    currentNode = linkedList
    while currentNode != None:
        nextNode = currentNode.next
        while nextNode != None and nextNode.value == currentNode.value:
            nextNode = nextNode.next

        currentNode.next = nextNode
        currentNode = nextNode

    return linkedList