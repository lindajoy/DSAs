# Linked lists.
"""
A singly linked list contains a Node class and a linkedlist class.

Node class has two components: Data and pointer

Data  => Is the value you want to store in the node
Pointer => Refers to the next node in the list. It is essential for connectivity.
"""

# Difference between lists and Linked lists is the way elements are inserted and deleted.
"""
Linked Lists => Insertion and deletion at the head happedn in a constant time, whereas at tail, it takes O(n) time.

Lists => It takes O(N) time to insert or delete a value.
Lists are arranged contingously in memory while nodes in a linked list may be dispersed in the memory.

This memory layout also affects access operation: Contingous layout of lists allows us to  index the list ; thus, access operation in the list is O(1) whereas for a linked list, 
we need to perform a traversal thus, it becomes O(n).

In a linked list, insertion and deletion happen in a constant amount of time given the pointer of the node to be deleted/inserted.
In linked lists, there is no concept of indexing. To reach a certain element in the list, we must traverse it from the beginning.

Note:* Insertion at tail for arrays like data structures is in O(n), but in python, the append method for lists is able to do it in O(1).
Note:** Deletion at tail for arrays like data structures is in O(n), but in python, the pop method for lists is able to do it in O(1).
"""

# BASIC LINKED LIST OPERATIONS.

class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None

class LinkedList:
    def __init__(self):
        self.head_node = None

    # Insertion at head
    def insert_at_head(self, data):
        # Create a new node containing your specified value
        temp_node = Node(data)
        # The new node points to the same node as the head
        temp_node.next_element = self.head_node
        self.head_node = temp_node # make the head point to the new node
        return self.head_node # return the new list

    def get_head(self):
        return self.head_node
    
    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False
    
    
lst = LinkedList()
print('Here is my list head Node:',lst.get_head())

# The time complexity for get_head() is O(1) as we simply return the head

# IS_EMPTY()
# The basic condition for our list to be considered empty is that there are no nodes in the list.
# This implies that head points to None.
# (SEE UP THERE)

print(lst.is_empty())

# SINGLY LINKED LIST INSERTION
"""
TYPES OF INSERTION:
    1. Insertion at the head
    2. Insertion at the tail
    3. Insertion at the kth index
"""
