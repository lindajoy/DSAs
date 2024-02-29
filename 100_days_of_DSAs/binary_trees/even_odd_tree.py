"""
EVEN ODD TREE

A binary tree is named Even-Odd if it meets the following conditions:

    The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
    For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
    For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).

Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.
"""

# Whenever you come across a Tree question, It is possible for us to solve it using either a BFS or DFS.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS  => Level order Traversal.
# O(N) time complexity n being the number of nodes
        
# Whenever you come across a question involving trees, Your first thought should be either of the two algorithms: BFS and DFS
        
from collections import deque

def isEvenOddTree(root: TreeNode):
    even = True
    q = deque([root])

    while q:
        prev = float("-inf") if even else float("inf")

        for _ in range(len(q)):
            node = q.popleft()

            if even and (node.val % 2 == 0 or node.val <= prev):
                return False
            elif not even and (node.val % 2 == 1 or node.val >= prev):
                return False
            
            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

            prev = node.val
        even = not even

    return True




