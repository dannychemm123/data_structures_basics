class LinkedList:
    """Linked List implementation in Python
    
    Attributes:
        value: The value stored in the node
        next: A reference to the next node in the linked list
    
    Methods:
        __init__: Initializes a new node with a value and an optional next node
        __str__: Returns a string representation of the node's value"""
    def __init__(self,value,next = None):
        self.value = value
        self.next = next
    

    def __str__(self):
        return str(self.value)
    
Head = LinkedList(1)
A = LinkedList(3)
B = LinkedList(4)
C = LinkedList(7)

Head.next = A
A.next = B
B.next = C

print("Linked List: ")


# Using while loop to print the linked list
current_node = Head
while current_node is not None:
    print(current_node.value)
    current_node = current_node.next

# Let display the linked list => O(n) time complexity

def display_linked_list(head):
    """Displays the values of the linked list starting from the head node
    
    Args:
        head: The head node of the linked list"""
    current_node = head
    elements = []
    while current_node is not None:
        elements.append(str(current_node.value))
        current_node = current_node.next
    print(" -> ".join(elements))

display_linked_list(Head)

# Searching for a value in the linked list => O(n) time complexity
def search_linked_list(head, target):
    """Searches for a target value in the linked list starting from the head node
    
    Args:
        head: The head node of the linked list
        target: The value to search for in the linked list """
    current_node = head
    while current_node is not None:
        if current_node.value == target:
            return f'Value {target} found in the linked list.'
        current_node = current_node.next
    return f'Value {target} not found in the linked list.'

print(search_linked_list(Head, 4))  # Output: Value 4 found in the linked list.
print(search_linked_list(Head, 10)) # Output: Value 10 not found

class DoublyLinkedList:
    """Doubly Linked List implementation in Python
    
    Attributes:
        value: The value stored in the node
        next: A reference to the next node in the linked list
        prev: A reference to the previous node in the linked list
    
    Methods:
        __init__: Initializes a new node with a value, an optional next node, and an optional previous node
        __str__: Returns a string representation of the node's value"""
    def __init__(self,value,next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev
    

    def __str__(self):
        return str(self.value)
def display_doubly_linked_list(head):
    """Displays the values of the doubly linked list starting from the head node
    
    Args:
        head: The head node of the doubly linked list"""
    current_node = head
    elements = []
    while current_node is not None:
        elements.append(str(current_node.value))
        current_node = current_node.next
    print(" <-> ".join(elements))
# Example usage of DoublyLinkedList
Head = Tail= DoublyLinkedList(1)

# Inserting nodes at the beginning

def insert_at_beginning(head, tail, value):
    """Inserts a new node with the given value at the beginning of the doubly linked list
    
    Args:
        head: The head node of the doubly linked list
        tail: The tail node of the doubly linked list
        value: The value to be inserted at the beginning of the linked list"""
    new_node = DoublyLinkedList(value, next=head)
    head.prev = new_node
    return new_node, tail

Head, Tail = insert_at_beginning(Head, Tail, 0)
display_doubly_linked_list(Head) 

# Inserting nodes at the end
def insert_at_end(head, tail, value):
    """Inserts a new node with the given value at the end of the doubly linked list
    
    Args:
        head: The head node of the doubly linked list
        tail: The tail node of the doubly linked list
        value: The value to be inserted at the end of the linked list"""
    new_node = DoublyLinkedList(value, prev=tail)
    tail.next = new_node
    return head, new_node
Head,Tail = insert_at_end(Head,Tail,7)
display_doubly_linked_list(head=Head)
# Inserting nodes at a specific position
def insert(head,tail,value,position):
    """Inserts a new node with the given value at a specific position in the doubly linked list
    
    Args:
        head: The head node of the doubly linked list
        tail: The tail node of the doubly linked list
        value: The value to be inserted in the linked list
        position: The position at which to insert the new node (0-based index)"""
    new_node = DoublyLinkedList(value)
    if position == 0:
        return insert_at_beginning(head, tail, value)
    
    current_node = head
    current_position = 0

    while current_node is not None and current_position < position:
        current_node = current_node.next
        current_position += 1

    if current_node is None:
        return insert_at_end(head, tail, value)
    new_node.prev = current_node.prev
    new_node.next = current_node
    if current_node.prev is not None:
        current_node.prev.next = new_node
    current_node.prev = new_node
    if current_node == head:
        head = new_node
    return head, tail
Head,Tail = insert(Head,Tail,5,2)
display_doubly_linked_list(Head)  

    
