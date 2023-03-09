"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can 
be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

"""
Naive Approach: Declaring a hash set
"""
class Solution(object):
    def hasCycle(self, head):
       visited = set()

       while head and head.next:
          if head.next in visited:
            return True
          visited.add(head.next)
          head = head.next

       return False

x = Solution()
head = [3,2,0,-4]  
print(x.hasCycle(head))

"""
Optimized approach using Floyd's Tortoise and hare (Fast and slow pointers)
"""

class Solution(object):
    def hasCycle(self, head):
       slow, fast = head, head

       while fast and fast.next:
          slow = slow.next
          fast = fast.next.next

          if slow == fast:
            return True

       return False

          
