# A Stack is a linear data structure that follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out). LIFO implies that the element that is inserted last, comes out first and FILO implies that the element that is inserted first, comes out last.

# It behaves like a stack of plates, where the last plate added is the first one to be removed. Think of it this way:

# Pushing an element onto the stack is like adding a new plate on top.

# Popping an element removes the top plate from the stack.ypes of Stack:

# Types of Stack:

# Fixed Size Stack:
    
# A fixed size stack has a predefined capacity.

# Once it becomes full, no more elements can be added (this causes overflow).

# If the stack is empty and we try to remove an element, it causes underflow.

# Typically implemented using a static array.



# Dynamic Size Stack
# A dynamic size stack can grow and shrink automatically as needed.

# If the stack is full, its capacity expands to allow more elements.

# As elements are removed, memory usage can shrink as well.

# Can be implemented using:
# -> Linked List → grows/shrinks naturally.
# -> Dynamic Array (like vector in C++ or ArrayList in Java) → resizes automatically.

# Example: Stack implementation using linked list or resizable array.

# Note: We generally use dynamic stacks in practice, as they can grow or shrink as needed without overflow issues.





# Common Operations on Stack:

# In order to make manipulations in a stack, there are certain operations provided to us.

# push() to insert an element into the stack.
# pop() to remove an element from the stack.
# top() Returns the top element of the stack.
# isEmpty() returns true if stack is empty else false.
# size() returns the size of the stack.





# Stack using Array
# A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. It can be implemented using an array by treating the end of the array as the top of the stack.



# Operations On Stack

# Push Operation:
# Adds an item to the stack. If the stack is full, then it is said to be an Overflow condition.

# Before pushing the element to the stack, we check if the stack is full.

# If the stack is full (top == capacity-1) , then Stack Overflows and we cannot insert the element to the stack.

# Otherwise, we increment the value of top by 1 (top = top + 1) and the new value is inserted at top position .

# The elements can be pushed into the stack till we reach the capacity of the stack.


# def push(self, x):
    
#     if self.top == self.capacity - 1:
#         print("Stack Overflow")
#         return
    
#     self.top += 1
    
#     self.arr[self.top] = x

# Time Complexity: O(1)
# Auxiliary Space: O(1)





# Pop Operation:

# Removes an item from the stack. The items are popped in the reversed order in which they are pushed. If the stack is empty, then it is said to be an Underflow condition.

# Before popping the element from the stack, we check if the stack is empty .

# If the stack is empty (top == -1), then Stack Underflows and we cannot remove any element from the stack.

# Otherwise, we store the value at top, decrement the value of top by 1 (top = top – 1) and return the stored top value.


# def pop(self):
    
#     if self.top == -1:
#         print("Stack Underflow")
#         return -1
    
#     value = self.arr[self.top]
#     self.top -= 1
 
#     return value

# Time Complexity: O(1)
# Auxiliary Space: O(1)


# Top or Peek Operation in Stack:

# Returns the top element of the stack.

# Before returning the top element from the stack, we check if the stack is empty.
# If the stack is empty (top == -1), we simply print “Stack is empty”.
# Otherwise, we return the element stored at index = top.

# def peek(self):
  
#     if self.top == -1:
#         print("Stack is Empty")
#         return -1
  
#     return self.arr[self.top]

# Time Complexity: O(1)
# Auxiliary Space: O(1)



# isEmpty Operation in Stack:

# Returns true if the stack is empty, else false.

# Check for the value of top in stack.
# If (top == -1) , then the stack is empty so return true.
# Otherwise, the stack is not empty so return false.


# def isEmpty(self):
#     return self.top == -1

# Time Complexity: O(1)
# Auxiliary Space: O(1)




# isFull Operation in Stack :

# Returns true if the stack is full, else false.

# Check for the value of top in stack.
# If (top == capacity-1), then the stack is full so return true.
# Otherwise, the stack is not full so return false.

# def isFull(self):
#     return self.top == self.capacity - 1

# Time Complexity: O(1)
# Auxiliary Space: O(1)


# Full Implementation of Stack using Array
class myStack:
    # constructor
    def __init__(self, cap):
        self.capacity = cap
        self.arr = [0] * self.capacity
        self.top = -1

    # push operation
    def push(self, x):
        if self.top == self.capacity - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.arr[self.top] = x

    # pop operation
    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return -1
        val = self.arr[self.top]
        self.top -= 1
        return val

    # peek (or top) operation
    def peek(self):
        if self.top == -1:
            print("Stack is Empty")
            return -1
        return self.arr[self.top]

    # check if stack is empty
    def isEmpty(self):
        return self.top == -1

    # check if stack is full
    def isFull(self):
        return self.top == self.capacity - 1


if __name__ == "__main__":
    st = myStack(4)

    # pushing elements
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)

    # popping one element
    print("Popped:", st.pop())

    # checking top element
    print("Top element:", st.peek())

    # checking if stack is empty
    print("Is stack empty: ", "Yes" if st.isEmpty() else "No")

    # checking if stack is full
    print("Is stack full: ", "Yes" if st.isFull() else "No")
    

# Output
# Popped: 4
# Top element: 3
# Is stack empty: No
# Is stack full: No



# Stack Implementation using Dynamic Array
class myStack:
    def __init__(self):
        self.arr = []

    # push operation
    def push(self, x):
        self.arr.append(x)

    # pop operation
    def pop(self):
        if not self.arr:
            print("Stack Underflow")
            return -1
        return self.arr.pop()

    # peek operation
    def peek(self):
        if not self.arr:
            print("Stack is Empty")
            return -1
        return self.arr[-1]

    # check if stack is empty
    def isEmpty(self):
        return len(self.arr) == 0

    # current size
    def size(self):
        return len(self.arr)


if __name__ == "__main__":
    st = myStack()

    # pushing elements
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)

    # popping one element
    print("Popped:", st.pop())

    # checking top element
    print("Top element:", st.peek())

    # checking if stack is empty
    print("Is stack empty:", "Yes" if st.isEmpty() else "No")

    # checking current size
    print("Current size:", st.size())
    
# Output
# Popped: 4
# Top element: 3
# Is stack empty: No
# Current size: 3 




# Stack - Linked List Implementation
# A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. It can be implemented using a linked list, where each element of the stack is represented as a node. The head of the linked list acts as the top of the stack.

# Declaration of Stack using Linked List
# A stack can be implemented using a linked list where we maintain:

# A Node structure/class that contains:
# data → to store the element.
# next → pointer/reference to the next node in the stack.
# A pointer/reference top that always points to the current top node of the stack.
# Initially, top = null to represent an empty stack.

# # Node structure
# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.next = None


# # Stack class
# class myStack:
#     def __init__(self):
        
#         # initially stack is empty
#         self.top = None




# Operations on Stack using Linked List

# Push Operation
# Adds an item to the stack. Unlike array implementation, there is no fixed capacity in linked list. Overflow occurs only when memory is exhausted.

#  A new node is created with the given value.
# The new node’s next pointer is set to the current top.
# The top pointer is updated to point to this new node.


# def push(self, x):
#     temp = Node(x)
#     temp.next = self.top
#     self.top = temp

# Time Complexity: O(1)
# Auxiliary Space: O(1)



# Pop Operation

# Removes the top item from the stack. If the stack is empty, it is said to be an Underflow condition.

# Before deleting, we check if the stack is empty (top == NULL).
# If the stack is empty, underflow occurs and deletion is not possible.
# Otherwise, we store the current top node in a temporary pointer.
# Move the top pointer to the next node.
# Delete the temporary node to free memory.

# def pop(self):
   
#     if self.top is None:
#         print("Stack Underflow")
#         return -1

#     temp = self.top
#     self.top = self.top.next
#     val = temp.data

#     del temp
#     return val


# Time Complexity: O(1)
# Auxiliary Space: O(1)



# Peek (or Top) Operation
# Returns the value of the top item without removing it from the stack.

# If the stack is empty (top == NULL), then no element exists.
# Otherwise, simply return the data of the node pointed by top.

# def peek(self):
 
#     if self.top is None:
#         print("Stack is Empty")
#         return -1
 
#     return self.top.data


# Time Complexity: O(1)
# Auxiliary Space: O(1)




# isEmpty Operation
# Checks whether the stack has no elements.

# If the top pointer is NULL, it means the stack is empty and the function returns true.
# Otherwise, it returns false.

# def isEmpty(self):
#     return self.top is None

# Time Complexity: O(1)
# Auxiliary Space: O(1)



# Stack Implementation using Linked List

# Node structure
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Stack implementation using linked list
class myStack:
    def __init__(self):
        # initially stack is empty
        self.top = None
        self.count = 0

    # push operation
    def push(self, x):
        temp = Node(x)
        temp.next = self.top
        self.top = temp

        self.count += 1

    # pop operation
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return -1
        temp = self.top
        self.top = self.top.next
        val = temp.data

        self.count -= 1
        return val

    # peek operation
    def peek(self):
        if self.top is None:
            print("Stack is Empty")
            return -1
        return self.top.data

    # check if stack is empty
    def isEmpty(self):
        return self.top is None

    # size of stack
    def size(self):
        return self.count


if __name__ == "__main__":
    st = myStack()

    # pushing elements
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)

    # popping one element
    print("Popped:", st.pop())

    # checking top element
    print("Top element:", st.peek())

    # checking if stack is empty
    print("Is stack empty:", "Yes" if st.isEmpty() else "No")

    # checking current size
    print("Current size:", st.size())
    
    
# Output
# Popped: 4
# Top element: 3
# Is stack empty: No
# Current size: 3