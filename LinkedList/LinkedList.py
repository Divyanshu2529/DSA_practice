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
    
    
    
# Deletion at beginning (Removal of first node) in a Linked List

# To remove the first node of a linked list, store the current head in a temporary variable (temp), move the head pointer to the next node, delete the temporary head node and finally , return the new head of the linked list.


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


# Delete the head node and return the new head
def deleteHead(head):

    # Check if the list is empty
    if head is None:
        return None

    # Store the current head in a
    # temporary variable
    temp = head

    # Move the head pointer to the next node
    head = head.next

    # Free the memory of the old head node
    # (Python garbage collector will handle it)
    temp = None

    return head


# Function to print the linked list
def printList(curr):
    while curr is not None:
        print(curr.data, end="")
        if curr.next is not None:
            print(" -> ", end="")
        curr = curr.next


if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 8 -> 2 -> 3 -> 1 -> 7
    head = Node(8)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(7)

    head = deleteHead(head)  
    printList(head)

# Output: 2 -> 3 -> 1 -> 7

# O(1) Time and O(1) Space



# Deletion at end (Removal of last node) in a Linked List

# To perform the deletion operation at the end of linked list, we need to traverse the list to find the second last node, then set its next pointer to null. If the list is empty then there is no node to delete or has only one node then point head to null.

# Node class for the linked list
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


# Function to remove the last 
# node of the linked list
def removeLastNode(head):
    # If the list is empty, return None
    if head is None:
        return None

    # If the list has only one node, 
    # delete it and return None
    if head.next is None:
        return None

    # Find the second last node
    secondLast = head
    while secondLast.next.next is not None:
        secondLast = secondLast.next

    # Delete the last node by making 
    # second_last point to None
    secondLast.next = None

    return head


def printList(head):
    while head is not None:
        print(f"{head.data} -> ", end="")
        head = head.next
    print("None")


if __name__ == "__main__":
    # Creating a static linked list
    # 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # Removing the last node
    head = removeLastNode(head)

    printList(head)

# Output
# 1 -> 2 -> 3 -> 4 -> nullptr
# Time Complexity: O(n), traversal of the linked list till its end, so the time complexity required is O(n).
# Auxiliary Space: O(1)





# Delete Node from a specific Position

# To perform the deletion, If the position is 1, we update the head to point to the next node and delete the current head. For other positions, we traverse the list to reach the node just before the specified position. If the target node exists, we adjust the next of this previous node to point to next of next nodes, which will result in skipping the target node.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteNode(head, position):
    temp = head

    # Head is to be deleted
    if position == 1:
        head = temp.next
        return head

    # Traverse to the node before 
    # the one to be deleted
    prev = None
    for i in range(1, position):
        prev = temp
        temp = temp.next

    # Delete the node at the position
    prev.next = temp.next
    return head


def printList(head):
    while head is not None:
        print(f"{head.data} -> ", end="")
        head = head.next
    print("nullptr")


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    position = 3
    head = deleteNode(head, position)

    printList(head)
    
    
# Output: 1 -> 2 -> 4 -> nullptr
# O(n) Time and O(1) Space




# Search an element in a Linked List

# [Approach 1] Iterative Approach

# a Linked List Node
class Node:
  
  	# constructor to intialize a node with data
    def __init__(self, x):
        self.data = x
        self.next = None

# checks whether key is present in linked list
def search_key(head, key):
  
    # initialize curr with the head of linked list
    curr = head

    # iterate over all the nodes
    while curr is not None:

        # if the current node's value is equal to key,
        # return true
        if curr.data == key:
            return True

        # move to the next node
        curr = curr.next

    # if there is no node with value as key, return false
    return False

if __name__ == "__main__":

    # create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # key to search in the linked list
    key = 5

    if search_key(head, key):
        print("true")
    else:
        print("false")
        
# Output: True
# O(n) Time and O(1) Space


# [Approach 2] Recursive Approach
# a Linked List Node
class Node:
  
  	# constructor to initialize a new node with data
    def __init__(self, x):
        self.data = x
        self.next = None

# checks whether the key is present in linked list
def searchKey(head, key):
  
    # base case
    if head is None:
        return False

    # if key is present in current node, return true
    if head.data == key:
        return True

    # recur for remaining list
    return searchKey(head.next, key)

if __name__ == "__main__":
  
    # create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # key to search in the linked list
    key = 5

    if searchKey(head, key):
        print("true")
    else:
        print("false")
        
# Output:True
# O(n) Time and O(n) Space





# Modify contents of Linked List

# Naive Approach] Change Linked List to Array

# Python program to modify a singly linked list
# By transferring it to an array

# The idea is to take out all elements from LinkedList add them into an array and apply the required operations:  For each node in the first half of the list, its value is changed by subtracting it from the corresponding value in the second half of the list (from the end towards the center). After performing these modifications, the values in the first half of the array are swapped with the corresponding values in the second half on the array and then put back all elements into the LinkedList.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def countNodes(head):
    count = 0
    curr = head

    while curr is not None:
        count += 1
        curr = curr.next

    return count

def linkedListToArray(head, arr, n):
    curr = head

    for i in range(n):
        arr[i] = curr.data
        curr = curr.next

def arrayToLinkedList(arr, head, n):
    curr = head

    for i in range(n):
        curr.data = arr[i]
        curr = curr.next

def modifyArray(arr, n):
  
    # Modify the array
    for i in range(n // 2):
        x = arr[i]
        arr[i] = arr[n - i - 1] - x
        arr[n - i - 1] = x

def modifyTheList(head):
    if head.next is None:
        return None

    # Count the number of nodes
    n = countNodes(head)

    # Create an array
    arr = [0] * n

    # Convert linked list to array
    linkedListToArray(head, arr, n)

    # Modify the array
    modifyArray(arr, n)

    # Convert array back to linked list
    arrayToLinkedList(arr, head, n)

    return head

def printList(node):
    curr = node
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":

    # Create a hard-coded linked list
    # 10 -> 4 -> 5 -> 3 -> 6
    head = Node(10)
    head.next = Node(4)
    head.next.next = Node(5)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(6)

    head = modifyTheList(head)

    printList(head)
    
# Output: -4 -1 5 4 10 
# O(n) Time and O(n) Space






# [Expected Approach] Reverse the 2nd Half Twice

# The idea is to handle the modification of a singly linked list by reversing its second half to allow traversal in both directions. First, find the middle of the list and reverse the second half starting from the node after the middle. Then, traverse the first half and the reversed second half simultaneously, updating the first half's node values by subtracting their values from the corresponding nodes in the second half and swapping them. After the traversal, reverse the modified second half again to restore its original order. Finally, reconnect the first and restored second halves to complete the list modification.

# Python program to modify a singly linked list
# By Reversing the 2nd Half Twice 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to reverse a linked list iteratively
def reverse(head):
  
    # Initialize previous, current,
    # and next pointers
    prev = None
    curr = head

    # Traverse and reverse the linked list
    while curr is not None:
        next_node = curr.next

        # Reverse the current node's pointer
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

# Function to modify the linked list
def modifyTheList(head):
  
    # Returning head if list has only one node
    if head.next is None:
        return head

    slow = head
    fast = head

    # Finding the middle node of the linked list
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    mid = slow

    # Storing the second half of the list starting
    # after the middle node
    reversed_list = mid.next

    # Splitting the list into two halves
    mid.next = None

    # Reversing the second half of the list
    reversed_list = reverse(reversed_list)

    curr1 = head
    curr2 = reversed_list

    # Iterating over both halves of the list 
    # and modifying the values
    while curr2 is not None:
        x = curr1.data
        curr1.data = curr2.data - x
        curr2.data = x
        curr1 = curr1.next
        curr2 = curr2.next

    # Reversing the second half of the list 
    # again and connecting both halves
    mid.next = reverse(reversed_list)
    
    return head

def print_list(node):
    curr = node
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next

if __name__ == "__main__":
  
    # Create a hard-coded linked list
    # 10 -> 4 -> 5 -> 3 -> 6
    head = Node(10)
    head.next = Node(4)
    head.next.next = Node(5)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(6)

    head = modifyTheList(head)

    print_list(head)
    
# Output: -4 -1 5 4 10 
# O(n) Time and O(1)







# Reverse a Linked List

# Approach] Using Iterative Method

# The idea is to reverse the linked list by changing the direction of links using three pointers: prev, curr, and next. At each step, point the current node to its previous node and then move all three pointers forward until the list is fully reversed.

class Node:
    def __init__(self,x):
        self.data = x
        self.next = None
        
def reverseList(head):
    curr = head
    prev = None
    
    while curr is not None:
        nextNode = curr.next 
        curr.next = prev
        
        
        prev = curr
        curr = nextNode
        
    return prev

def printList(node):
    while node is not None:
        print(f"{node.data}", end ="")
        if node.next is not None:
            print("-->", end ="")
        node = node.next 
    print()

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head = reverseList(head)
    printList(head)

# Output: 5 -> 4 -> 3 -> 2 -> 1
# O(n) Time and O(1) Space




# [Alternate Approach 1] Using Recursion Method

class Node:
    def __init__(self, newData):
        self.data = newData
        self.next = None

def reverseList(head):
    if head is None or head.next is None:
        return head

    # reverse the rest of linked list and put the
    # first element at the end
    rest = reverseList(head.next)

    # make the current head as last node of
    # remaining linked list
    head.next.next = head

    # update next of current head to NULL
    head.next = None

    return rest


def printList(node):
    while node is not None:
        print(f"{node.data}", end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next
    print()


if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head = reverseList(head)
    printList(head)


# O(n) Time and O(n) Space
# Output: 5 -> 4 -> 3 -> 2 -> 1