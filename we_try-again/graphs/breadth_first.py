"""
You're given a Node class that has a name and an array of optional children nodes.
When put together, nodes form an acyclic tree-like structure.

Implement the breadthFirstSearch method on the Node class, which takes in an empty array, traverses the tree using the Breadth-first Search approach 
(specifically navigating the tree from left to right), 
stores all of the nodes' names in the input array, and returns it.

If you're unfamiliar with Breadth-first Search, we recommend watching the Conceptual Overview section of this question's video explanation before starting to code.

Sample Input: 
graph = A
     /  |  \
    B   C   D
   / \     / \
  E   F   G   H
     / \   \
    I   J   K

Sample Output: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]

With Breadth First Search, We go level by level.
With Bfs, we are always sure that we are going to use the queue data structure.
"""

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]  # Initialize queue with root node
        while queue:
            current_node = queue.pop(0)  # Dequeue the first node
            array.append(current_node.name)  # Append current node's name to result
            for child in current_node.children:
                queue.append(child)  # Enqueue children of the current node
        return array

# Example usage:
# Constructing a tree
root = Node("A")
root.add_child("B").add_child("C").add_child("D")
root.children[0].add_child("E").add_child("F")
root.children[2].add_child("G").add_child("H")

# Performing breadth-first search
result = root.breadthFirstSearch([])
print(result)  # Output: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
