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







