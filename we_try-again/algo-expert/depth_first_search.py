"""
Depth First Search

You're given a Node class that has a name and an array of optional children nodes. 
When put together, nodes form an acyclic tree-like structure.

Implement the depthFirstSearch method on the Node class, which takes in an empty array,
traverses the tree using the Depth-first Search approach (specifically navigating the tree from left to right), 
stores all of the nodes' names in the input array, and returns it.

If you're unfamiliar with Depth-first Search, we recommend watching the Conceptual Overview section of this question's video explanation before starting to code.


graph = A
     /  |  \
    B   C   D
   / \     / \
  E   F   G   H
     / \   \
    I   J   K

Should return: ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]

"""

# One thing to note here is that the node class will always consist of a name and array of children.
# A question to ask the interviewer would be is the name of the  node the value we are particularly interested in adding on an array?
# 🙃 Acyclic means no cycle in the graph 🙃

# Whats the input? A node class
# Whats the output? A list containing the values

#💡  A node class has name and  a list of children

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)
    
    def depthFirstSearch(self, result=[]):
        # Append the current node's name to the result array
        result.append(self.name)

        # Recursively traverse each child in depth-first manner
        for child in self.children:
            child.depthFirstSearch(result)

        return result

# Example Usage:
# Create a tree
root = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")

root.add_child(node_b)
root.add_child(node_c)
node_b.add_child(node_d)
node_b.add_child(node_e)
node_c.add_child(node_f)

# Call depthFirstSearch on the root node
result = root.depthFirstSearch()
print(result)
