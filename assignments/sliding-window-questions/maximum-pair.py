"""
Given an array as input, 
extract the pair of contiguous integers that have the highest sum of all pairs. Return the pair as an array.

Example: [5, 2, 4, 6, 3, 1]  
Output here of the maximum pair could be: [4,6]
"""

def max_pair(arr):
    n = len(arr)
    curr_pair = [arr[0], arr[1]]
    max_pair = curr_pair[:]
    print(max_pair)
    
    for i in range(2, n):
        pair_sum = arr[i-1] + arr[i]
        if pair_sum > sum(curr_pair):
            curr_pair = [arr[i-1], arr[i]]
        if sum(curr_pair) > sum(max_pair):
            max_pair = curr_pair[:]
    
    return max_pair


x = [5, 2, 4, 6, 3, 1]  
print(max_pair(x))


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        first_set=set()
        curr=headA
        
        while curr:
            first_set.add(curr)
            curr=curr.next
        
        curr = headB
        while curr:
            if curr in first_set:
                return curr
            curr=curr.next

        return None