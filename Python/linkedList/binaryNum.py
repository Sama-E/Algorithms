# A number is represented as a series of 0's and 1's. In this challenge, the series
# will be in the form of a singly-linked list. Each node instance, a Linked List Node,
# has a value, data, and a pointer to the next node, next. Given a reference to the head 
# of a singly-linked list, convert the binary number represented to a decimal number.

list = [0, 0, 1, 1, 0, 1, 0]
output = 26

list1 = [0, 0, 0, 0, 1, 1, 1, 1]
output = 31


#
# Complete the 'getNumber' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_SINGLY_LINKED_LIST binary as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

# Python3 program to find decimal value 
# of binary linked list

# Node Class
class Node:
    
    # Function to initialise the 
    # node object
    def __init__(self, data):
        
        # Assign data
        self.data = data 
        
        # Initialize next as null
        self.next = None

# Linked List class contains 
# a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        
        self.head = None

    # Returns decimal value of binary
    # linked list
    def decimalValue(self, head):
        
        # Initialized result
        res = 0

        # Traverse linked list
        while head:

            # Multiply result by 2 and 
            # add head's data 
            res = (res << 1) + head.data

            # Move Next
            head = head.next
            
        return res

# Driver code
if __name__ == '__main__':

    #Start with the empty list 
    llist = LinkedList()

    llist.head = Node(0)
    llist.head.next = Node(0)
    llist.head.next.next = Node(1)
    llist.head.next.next.next = Node(1)
    llist.head.next.next.next.next = Node(0)
    llist.head.next.next.next.next.next = Node(1)
    llist.head.next.next.next.next.next.next = Node(0)
    
    print("Decimal Value is {}".format(
          llist.decimalValue(llist.head)))