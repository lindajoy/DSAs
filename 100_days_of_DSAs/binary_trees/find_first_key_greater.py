"""
FIND THE FIRST KEY GREATER THAN A GIVEN VALUE IN BST.

Write a program that takes as input a BST and 
a value, and retums the first key that would appear in an inorder traversal which is greater than the input value. 
"""

# What is the question? Find the first value which is greater and returns the first key that would appear
# in an in order traversal which is greater than the input value.

# InOrder => Left, Root, Right
# PostOrder => Left, Right, Root
# PreOrder => Root, Left, Right

# We can find the desired node in O(N) time where n is the number of nodes in the BST, by doing an inorder walk.
# This approach does not use the BST property.

# A better approach is to use the BST search idiom.
# We store the best candidate for the result and update the candidate as we iteratively descend the tree, eliminating subtres by comparing the keys stored at nodes with the input value.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# So here we have eliminated unecessary traversal in our tree that does not make sense at the moment.

# The space complexity of this is O(1)
# The time complexity of this is O(h)
def find_first_greater_than_k(tree: TreeNode, k):
    subtree, first_so_far = tree, None
    while subtree:
        if subtree.val > k:
            first_so_far, subtree = subtree, subtree.left
        else:
            subtree = subtree.right

    return first_so_far

# Finding First Value That is greater... 
# Hey! Breathe in,  You got this.

# 😄🤔

def find_first_val_greater_than_k(root: TreeNode, target):
    if root is None:
        return None
    successor  = root

    while root:
        if root.val > target:
            successor = root
            root = root.left
        else:
            root = root.right

    return successor if successor else None

# A variant to the first question.

"""
Write a program that takes as input a BST and a value,
and returns the node whose key equals the input value 
and appears first in an inorder traversal of the BST. 
For example, when applied to the BST,
your program should return Node B for 108,
Node G for 285, and null for 143.
"""

# Here we are Traversing through the tree Node to find the element that is the first to be equal to the target.
# Hey dont give up? Okay? 
# Hey Breathe ~

from collections import deque

def find_first_occurence(tree: TreeNode, target):
    if not tree:
        return None
    
    queue = deque([tree])

    while queue:
        node = queue.pop(0)
        if node.val == target:
            return node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return None
    
    
