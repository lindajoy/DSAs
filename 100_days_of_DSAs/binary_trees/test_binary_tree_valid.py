"""
Test if a binary tree satisfies the BST Property

Write a program that takes an input as a binary tree and checks if it satisifies the BST property.
"""

# How do we know that our Binary Tree is Valid?

# The rule is that the value of a left node must be smaller than its parent node.
# The value at the right node must be greater than its parent node.
# The rule is repeated over and over again for the left and right parts of the tree, starting from the main starting point called the root.

# Starting to make sense.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    
    # The value at the left must be less than the root.
    # The value at the right must be greater than the root.
    if root.val <= min_val or root.val >= max_val:
        return False
    
    return (is_valid_bst(root.left, min_val, root.val) or
            is_valid_bst(root.right, max_val, root.val))
    