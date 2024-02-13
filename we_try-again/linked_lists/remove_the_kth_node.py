"""
💡 REMOVE THE KTH NODE FROM END

Write a function that takes in the head of a Singly Linked List and an integer k and removes the kth node from the end of the list.

The removal should be done in place, meaning that the original data structure should be mutated (no new structure should be created).

Furthermore, the input head of the linked list should remain the head of the linked list after the removal is done, 
even if the head is the node that's supposed to be removed. 
In other words, if the head is the node that's supposed to be removed, your function should simply mutate its value and next pointer.

Note that your function doesn't need to return anything.

You can assume that the input Linked List will always have at least two nodes and, more specifically, at least k nodes.

Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of the list.

"""

# Example 1

# INPUT

# head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 // the head node with value 0
# k = 4

# Output should be something like this or rather our mutated list should be:
# The 4th node from the end of the list (the node with value 6) is removed.
# 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9

# I always like initializing the listNode Class

class ListNode:
    def __init__(self, value, next):
        self.next = next
        self.value = value

# Solution using Two pointers; Fast and slow pointers solution.

def removeNthNodeFromEnd(head: ListNode, n: int) -> ListNode:
    # Initialize the slow and fast pointer
    slow = head
    fast = head

    for _ in range(n):
        fast = fast.next
    if not fast:
        head.next
    
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next

    return head
