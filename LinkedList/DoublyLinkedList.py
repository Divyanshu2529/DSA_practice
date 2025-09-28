# A doubly linked list is a more complex data structure than a singly linked list, but it offers several advantages. The main advantage of a doubly linked list is that it allows for efficient traversal of the list in both directions. This is because each node in the list contains a pointer to the previous node and a pointer to the next node. This allows for quick and easy insertion and deletion of nodes from the list, as well as efficient traversal of the list in both directions.


# Creating a doubly linked list 

class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None

if __name__ == "__main__":
    # Create the first node (head of the list)
    head = Node(10)

    # Create and link the second node
    head.next = Node(20)
    head.next.prev = head

    # Create and link the third node
    head.next.next = Node(30)
    head.next.next.prev = head.next

    # Create and link the fourth node
    head.next.next.next = Node(40)
    head.next.next.next.prev = head.next.next

    # Traverse the list forward and print elements
    temp = head
    while temp is not None:
        print(temp.data, end="")
        if temp.next is not None:
            print(" <-> ", end="")
        temp = temp.next