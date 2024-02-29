# Binary Search Trees

Binary Search Trees are a workhorse of data structures and can be used to solve almost every data structures problem reasonably effeciently.

They offer the ability to effeciently search for a key as well as find the min and max elements, look for the successor or predecessor of a search key and enumerate the keys in a range in sorted order.

BSTs are similar to arrays in that the stored values ( the  "keys") are stored in sorted order.

However unlike with a sorted array, keys can be added to and deleted from a BST effeciently.

Key lookup, insertion and deletion take propotional to the height of the tree, which can in the worst case be O(n), if insertions and deletions are naively implemented.

However, there are implementations of insert and delete which guarantee that the tree has height O(log n).

A BST prototype is as follows:
 
```
class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right
```

# Binary Search Trees Boot Camp
Searching is the single most fundamental application of BSTs.
Unlike a hash table, a BST offers the ability to find the min and max elements, and find the next largest/next smallest element.

These operations, along with lookup, delete and find, take O(log n) for library implementations of BSTs. Both BSTs and hash tables use O(n) space - in practice, a BST uses slightly more space.

# The follwoing program demonstrates how to check if a given value is present in a BST.

```
def search_bst(tree, key):
    return (tree
            if not tree or tree.data == key else search_bst(tree.left.key)
            if key < tree.data else search bst(tree.right, key))
```

Since the program descends tree with in each step, spends O(1) time per level, the time complexity is O(h) where h is the height of the tree.

With binary Trees, the elements are arranged following a specific order. The rule is that the value of a left node must be smaller than its parent node, and the value of a right node must be greater than its parent node. This rule is repeated over and over again for the left and right parts of the tree, starting from the main starting point called the root.