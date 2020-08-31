"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value) # Wraps the given value in a ListNode
        self.length += 1 # Adds the node so plus 1 length

        if not self.head and not self.tail: # If there's no head or tail
            self.head = new_node # new node is both
            self.tail = new_node # new node is both
        else: # else
            new_node.next = self.head # the next node to the given is the old head
            self.head.prev = new_node # node behind old head is new node
            self.head = new_node # new node is the head


        
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        pass
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value) # Wraps the given value in a ListNode
        self.length += 1 # Adds the node so plus 1 length

        if not self.head and not self.tail: # If there's no head or tail
            new_node = self.head # new node is both
            new_node = self.tail # new node is both
        else:
            new_node.prev = self.tail # the node behind the new node is the old tail
            self.tail.next = new_node # old tail next node is new node
            self.tail = new_node # tail is new node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        pass
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass