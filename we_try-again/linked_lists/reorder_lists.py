"""
REORDER LISTS.

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""


# Its not sorted or anything.

# Example 1
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

# Example 2

# Input: head = [6,7,8,1,4,3]
# Output: [6,3,7,4,8,1]

class ListNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

    
def reorder_lists(head: ListNode):
    # Find the middle of the Linked list
    fast = slow = head

    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    second = slow.next
    prev = slow.next = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    # Merge the two halfs
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2
# No return needed since the reorder is done in place.
