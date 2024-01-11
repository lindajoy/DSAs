### Binary Search Trees

BSTs are a workhorse of data structures and can be used to solve every data structure problem reasonably effeciently.

They offer the ability to search for a key as well as find the min and max elements , look for the successor or predecessor of a search key(which itself need not to be present in the BST), and enumerate the keys in a range in sorted order.

BSTs are similar to arrays in that the stored values (the "keys") are stored in sorted order.

However unlike with a sorted array, keys can be added to and deleted from a BST effeciently.

#### Binary search trees
Searching is the single most funcamental application of BSTs. 
Unlike a hash table, a BST offers the ability to find the min and max elements, and find the next largest/next smallest element.

BST PROTOTYPE.

```
class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right
```

##### The following program demeonstrates how to check if a given value is present in a BST

# This is a recursive function

def search_bst(tree, key):
    return (tree
            if not tree or tree.data == key else search_bst(tree.left, key)
            if key < tree.data else search_bst(tree.right, key))



###### Hmm ...
With a BST you can iterate through elements in sorted order O(n) (regardless whether balanced)

Some problems need a combination of a BST and a hashtable.

The BST property is a global property - a binary tree may have the property that each node's key is greater than the key at its left child and smaller than the key at its right child, but it may not be a BST.