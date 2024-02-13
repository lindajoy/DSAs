"""
REMOVE DUPLICATES FROM  A SINGLY LINKED LIST

You're given the head of a Singly Linked List whose nodes are in sorted order with respect to their values. 
Write a function that returns a modified version of the Linked List that doesn't contain any nodes with duplicate values. 
The Linked List should be modified in place (i.e., you shouldn't create a brand new list), 
and the modified Linked List should still have its nodes sorted with respect to their values.

Each LinkedList node has an integer value as well as a next node pointing to 
the next node in the list or to None / null if it's the tail of the list.

"""

# What is the input? The head of sorted Singly Linked List.
# What is the output? Modified version without the duplicated values.


# Good Job Joy! 👏🏾 🥳

# 💡 Defining a list Node
class ListNode:
    def __init__(self, data, next):
       self.data = data
       self.next = next

def remove_duplicates(head: ListNode):
    if not head:
        return "Linked List is empty"
    current = head

    while current.next and current.next.next:
        if current.next.data == current.data:
            current.next = current.next.next
        else:
            current = current.next
    return head