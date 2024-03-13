"""
SUM OF LINKED LISTS.

You're given two Linked Lists of potentially unequal length. 
Each Linked List represents a non-negative integer, where each node in the Linked List is a digit of that integer, 
and the first node in each Linked List always represents the least significant digit of the integer. 
Write a function that returns the head of a new Linked List that represents the sum of the integers represented by the two input Linked Lists.

Each LinkedList node has an integer value as well as a next node pointing to
the next node in the list or to None / null if it's the tail of the list. 
The value of each LinkedList node is always in the range of 0 - 9.

Note: your function must create and return a new Linked List, and you're not allowed to modify either of the input Linked Lists.

"""

# Sample Input

# linkedListOne = 2 -> 4 -> 7 -> 1
# linkedListTwo = 9 -> 4 -> 5

# Sample Output

# 1 -> 9 -> 2 -> 2
# // linkedListOne represents 1742
# // linkedListTwo represents 549
# // 1742 + 549 = 2291


# 💩 First instinct when I saw the question, was to append all the values into  2 different lists, and add, then convert back to a linked list.

# A class is a blueprint of an object

# PSEUODOCODE:

#   Initialize a new linked list: Using the List Node Class. And also the carry.
#   Go through the loop if either l1, l2 or carry exists.
#   Compute the total sum, which would be equal to val1 + val2 + carry.
#   Find the value you would like to carry and the value that should be in the list node.
#   Return dummy_head.next

class ListNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

    def add_linked_lists(l1, l2):
        # Initialize a new linked list; Using the List Node class
        dummy_head = ListNode()
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            # 💡 Extracting the first and second value in the two linked lists.
            val1 = l1.value if l1 else 0
            val2 = l2.value if l2 else 0

            # Calculate the sum and carry for the current digit.
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            current_digit = total_sum % 10

            current.next = ListNode(current_digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next
        
