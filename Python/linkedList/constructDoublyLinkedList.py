# Write DoublyLinkedList class that has a head and a tail, both of 
# which point to either a linked list Node or None / null. The class 
# should support:
#     - Setting the head and tail of linked list.append
#     - Inserting nodes before and after other nodes as well as at 
#     given positions(the position of the head node is 1).
#     - Removing given nodes and removing nodes with given values.
#     - Searching for nodes with given values.

# Note that the setHead, setTail, insertBefore, insertAfter, 
# insertAtPosition, and remove methods all take in actual Nodes as 
# input parameters - not integers(except for insertPosition, which 
# also takes in an integer representing the position); this means 
# that you don't need to create any new Nodes in these methods. The
# input nodes that are already in the linked list, the methods will 
# effectively be moving the nodes within the linked list. You won't
# be told if the input nodes are already in the linked list, so your
# code will have to defensively handle this scenario.

# If you're doing this problem in an untyped language like Python or 
# Javascript, you may want to look at the various function signatures 
# in a typed language like Java or Typescript to get a better idea of 
# what each input parameter is.

# Each Node has an integer value as well as prev node and a next, both 
# of which can point to either another node or None / null.




class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def setHead(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)


    def setTail(self, node):
        if self.tail == None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev == None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert


    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert


    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node != None and currentPosition != position:
            node = node.next
            currentPosition += 1
            if node != None:
                self.insertBefore(node, nodeToInsert)
            else:
                self.setTail(nodeToInsert)

    
    def removeNodesWithValue(self, value):
        node = self.head
        while node != None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)


    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)


    def containsNodeWithValue(self, value):
        node = self.head
        while node != None and node.value != value:
            node = node.next
        return node != None


    def removenodeBindings(self, node):
        if node.prev != None:
            node.prev.next = node.next
        if node.next != None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None