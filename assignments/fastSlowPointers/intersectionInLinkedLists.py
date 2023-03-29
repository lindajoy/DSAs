"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.


LeetCode Linked = https://leetcode.com/problems/intersection-of-two-linked-lists/description/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        visitedNodes = set()
        curr = headA

        while curr:
          visitedNodes.add(curr)
          curr = curr.next

        curr = headB
        while curr:
          if curr in visitedNodes:
            return curr

          curr = curr.next

        return None