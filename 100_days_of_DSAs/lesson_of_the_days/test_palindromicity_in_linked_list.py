"""
TEST PALINDROMICITY IN LINKED LIST

Write a program that tests whether a singly linked list is palindromic.
"""
# 🤔 Whats the input? A singly linked list
# 💡  Whats the output? Testing out the palindromicity of a linked list.

# Initialize list Node

class ListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        
# Lets define the pseudocode to this issue:

# The process/ Pseudocode is the following:
        
#   Finding the middle and the end.
#   Reversing the second part of the linked list.
#   Comparing the linked list halves

# This approach has a time complexity of O(N) and space complexity of O(1)
        
# If you think about it; the simple questions concerning linked lists are what built up the solution:
        
    # Reversing a linked list: https://leetcode.com/problems/reverse-linked-list/description/
    # Finding the middle node in the linked list: 

def isPalindrome(head: ListNode):
    # finding the middle and end
    slow, fast = head, head


    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # reversing the second part of the linked list
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    # Comparing the linked list two halfs
    left, right = head, prev
    while right != slow:
        if left.val !=  right.val:
            return False
        left = left.next
        right = right.next
    return True