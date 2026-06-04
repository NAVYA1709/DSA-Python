#Linked list 
# 10 -> 20 -> 30 -> None
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# #Create Nodes
# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)
# #Connect them
# n1.next = n2
# n2.next = n3

# #Traversal
# temp = n1
# while temp is not None :
#     print(temp.data)
#     temp=temp.next

# Head stores starting node.
class LinkedList:
    def __init__(self):
        self.head = None
      
# Insert at End ⭐
    def append(self, data):
        new_Node = Node(data)

        if self.head is None :
            self.head = new_Node
            return
        temp = self.head

        while temp.next is not None :
            temp = temp.next
        temp.next = new_Node

    #display
    def display(self) :
        temp = self.head
        while temp is not None :
            print(temp.data,end="->")
            temp=temp.next
        print("None")

    #O(1)
    def insert_begin(self,data) :
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Delete First Node ⭐⭐
    def delete_beg(self) :
        if self.head is None:
            return 
        self.head = self.head.next
    
    #COUNT NODES
    def count_nodes(self) :
        count = 0
        temp=self.head
        while temp is not None :
            count+=1
            temp=temp.next
        print(count)

# Create Linked List object
ll = LinkedList()

# Insert nodes
ll.append(10)
ll.append(20)
ll.append(30)

#insert at beg
ll.insert_begin(5)

# Display
ll.display()
ll.count_nodes()
#
ll.delete_beg()
ll.display()
ll.count_nodes()

#raversal / printing
# while temp:
# Insertion at end
# while temp.next:
