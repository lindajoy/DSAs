"""
Write a function that takes in a Binary Search Tree (BST) 
and a target integer value and returns the closest value to 
that target value contained in the BST.

You can assume that there will only be one closest value.

Each BST node has an integer value, 
a left child node, and a right child node. 
A node is said to be a valid BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; 
and its children nodes are either valid BST nodes themselves or None / null.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Sample Input:

   tree =    10
           /     \
          5      15
        /   \   /   \
       2     5 13   22
     /           \
    1            14
    
   target = 12
"""

"""
Sample Output: 13

"""

# This answer was wrong
from collections import deque

def closestValue(root: TreeNode, target):
    # Initialize a q.
    q = deque([root])

    while q:
        node = q.popleft()

        subtract = node.val - target

        if subtract == 1:
            return node.val
        elif node.right:
            q.append(node.right)
        elif node.left:
            q.append(node.left)
    return -1

def closestValue(root: TreeNode, target: int) -> int:
    closest = float('inf')
    curr = root
    
    while curr:
        if abs(curr.val - target) < abs(closest - target):
            closest = curr.val
            
        if target < curr.val:
            curr = curr.left
        elif target > curr.val:
            curr = curr.right
        else:
            return curr.val
        
    return closest