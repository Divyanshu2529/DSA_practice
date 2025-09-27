# Linked List

# A linked list is a fundamental data structure in computer science. It mainly allows efficient insertion and deletion operations compared to arrays. 

# Linked List V/S Array

# Linked List:
# Data Structure: Non-contiguous
# Memory Allocation: Typically allocated one by one to individual elements
# Insertion/Deletion: Efficient
# Access: Sequential


# Array:
# Data Structure: Contiguous
# Memory Allocation: Typically allocated to the whole array
# Insertion/Deletion: Inefficient
# Access: Random



# Singly Linked-List
# A singly linked list is a fundamental data structure, it consists of nodes where each node contains a data field and a reference to the next node in the linked list. The next of the last node is null, indicating the end of the list. Linked Lists support efficient insertion and deletion operations.


# Example: Head --> 1 --> 2 --> 3 --> 4 --> Null

# In a singly linked list, each node consists of two parts: data and a pointer to the next node. This structure allows nodes to be dynamically linked together, forming a chain-like sequence.

# constructor to initialize a new node with data
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# Create the first node (head of the list)
head = Node(10)

# Link the second node
head.next = Node(20)

# Link the third node
head.next.next = Node(30)

# Link the fourth node
head.next.next.next = Node(40)

# printing linked list
temp = head
while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next
    

# Output: 10,20, 30,40


# Operations on Linked List: 

# 1) Traversal of Singly Linked List
 
 # Traversal of Singly Linked List (Iterative Approach)
 
 # a linked list node
class Node:

    # constructor to initialize a new node with data
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# function to traverse and print the singly linked list
def traverseList(head):
    while head is not None:
        print(head.data, end="")
        if head.next is not None:   
            print(" -> ", end="")
        head = head.next
    print()

if __name__ == "__main__":

    # create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 40
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    traverseList(head)
    
# Output: 10 -> 20 -> 30 -> 40

# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Auxiliary Space: O(1)



# Traversal of Singly Linked List (Recursive Approach)

# a linked list node
class Node:
    def __init__(self, data):
        # constructor to initialize a new node with data
        self.data = data
        self.next = None

# function to traverse and print the singly linked list
def traverseList(head):
    # base condition is when the head is None
    if head is None:
        print()
        return

    # printing the current node data
    print(head.data, end="")

    # print arrow if not the last node
    if head.next is not None:
        print(" -> ", end="")

    # moving to the next node
    traverseList(head.next)

if __name__ == "__main__":
    # create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 40
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    traverseList(head)
    
    
    
# Output:10 20 30 40 
# Time Complexity: O(n), where n is number of nodes in the linked list.
# Auxiliary Space: O(n) because of recursive stack space.





# Insert a Node at Front of a Linked List

# To insert a new node at the front, we create a new node and point its next reference to the current head of the linked list. Then, we update the head to be this new node. This operation is efficient because it only requires adjusting a few pointers.

# Define a node in the linked list
class Node:
    def __init__(self,x):
        self.data = x
        self.next = None
    
def insert_at_front(head, x):
    newNode = Node (x)
    newNode.next = head
    return newNode

def printList(head):
    curr = head
    while curr is not None:
        print(curr.data, end="")
        if curr.next is not None:
            print("-->", end="")
        curr = curr.next
    print()
    
if __name__ == '__main__':
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(5)    
    
    x = 1
    head = insert_at_front(head, x)
    
    printList(head)
# Output
# 1 -> 2 -> 3 -> 4 -> 5

# Time Complexity: O(1), We have a pointer to the head and we can directly attach a node and update the head pointer. So, the Time complexity of inserting a node at the head position is O(1).
# Auxiliary Space: O(1)




# Insert Node at the End of a Linked List

# Inserting at the end involves traversing the entire list until we reach the last node. We then set the last node's next reference to point to the new node, making the new node the last element in the list.

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def insertAtEnd(head, x):
    newNode = Node(x)
    
    if head is None:
        return newNode
    
    temp = head
    
    while temp.next is not None:
        temp = temp.next 
        
    temp.next = newNode
    
    return head

def printList(head):
    curr = head
    while curr is not None:
        print(curr.data, end="")
        if curr.next is not None:
            print("-->", end=" ")
        curr = curr.next 
    print()
    
        
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

head = insertAtEnd(head,6)

printList(head)

# Output
# 2 -> 3 -> 4 -> 5 -> 6 -> 1
# Time Complexity: O(n) where n is the length of the linked list
# Auxiliary Space: O(1)



# Insert a node at a specific position in a linked list

# The idea is simple: create a new node, then find the spot where it should be placed. Walk through the list until you reach the node just before that position. Link the new node’s next to the following node, and adjust the previous node’s next to point to the new node. 
# O(n) time and O(1) space:

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def insertPos(head, pos, val):

    if pos < 1:
        return head

    # head will change if pos = 1
    if pos == 1:
        newNode = Node(val)
        newNode.next = head
        return newNode

    curr = head

    # Traverse to the node just before the new node
    for i in range(1, pos - 1):
        if curr is None:
            return head
        curr = curr.next

    # If position is greater than number of nodes
    if curr is None:
        return head

    newNode = Node(val)

    # update the next pointers
    newNode.next = curr.next
    curr.next = newNode

    return head

def printList(head):
    curr = head
    while curr:
        print(curr.val, end="")
        if curr.next:
            print(" -> ", end="")
        curr = curr.next
    print()

if __name__ == "__main__":
    # Creating the list 1->2->4
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(4)
    
    val, pos = 3, 3
    head = insertPos(head, pos, val)
    printList(head)
    
    
    
    