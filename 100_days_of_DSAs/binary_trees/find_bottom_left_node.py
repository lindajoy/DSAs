"""
FIND BOTTOM LEFT TREE VALUE

Given the root of a binary tree, 
return the leftmost value in the last row of the tree.
"""
# Level order traversal.
# Similar to the BFS traversal.
# Definition for a binary tree node.

# BST using the BFS traversal where we do level based traversal.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Take away here was using the Breadth First Search Algorithm in looking for the most left value.
from collections import deque

def findBottomLeftTreeValue(root: TreeNode):
    q = deque([root])

    while q:
        node = q.popleft()
        if node.right: q.append(node.right)
        if node.left: q.append(node.left)
    return node.val



