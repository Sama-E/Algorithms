class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class singlyLinkedList:
    def __init__(self):
        self.head = Node()


    # Append single element method for the linked list
    def append(self, data):
      new_node = Node(data)
      current = self.head
      while current.next != None:
        current = current.next
      current.next = new_node

    
    # Display method for the linked list
    def display(self):
      singlyLL = []
      current = self.head
      while current.next != None:
        current = current.next
        singlyLL.append(current.data)
      print(singlyLL)


    # Print the length of linked list
    def length(self):
      current = self.head
      total = 0
      while current.next != None:
        total += 1
        current = current.next
      # print(total)
      return total


    # Extract element method of index
    def extract(self, index):
      if index >= self.length():
        print("Error: 'Extract' index out of range!")
        return None
      current_index = 0
      current = self.head
      while True:
        current = current.next
        if current_index == index:
          print(current.data) 
          return current.data
        current_index += 1


    # Delete element method of index
    def delete(self, index):
      if index >= self.length():
        print("Error: 'Delete' index out of range")
        return None
      current_index = 0
      current = self.head
      while True:
        last_node = current
        current = current.next
        if current_index == index:
          last_node.next = current.next
          return
        current_index += 1

    
    def arrayToLL(self, array):
      LL = []
      n = len(array)
      for i in range(0, n, 1):
        LL.append(array[i])
      print(LL)
      return LL




my_list = singlyLinkedList()

# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append(4)
# my_list.append(5)

# my_list.display()
# my_list.length()
# my_list.extract(2)
# my_list.delete(2)
# my_list.display()

array = [1,2,3,4,5,5,6,6]
my_list.arrayToLL(array)
my_list.display()
