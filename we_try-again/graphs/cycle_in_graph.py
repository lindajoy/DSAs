"""
CYCLE IN GRAPH

You're given a list of edges representing an unweighted, directed graph with at least one node. 
Write a function that returns a boolean representing whether the given graph contains a cycle.

For the purpose of this question, a cycle is defined as any number of vertices, including just one vertex, that are connected in a closed chain.
A cycle can also be defined as a chain of at least one vertex in which the first vertex is the same as the last.

The given list is what's called an adjacency list, and it represents a graph. 
The number of vertices in the graph is equal to the length of edges, where each index i in edges contains vertex i's outbound edges, in no particular order. 
Each individual edge is represented by a positive integer that denotes an index (a destination vertex) in the list that this vertex is connected to. 
Note that these edges are directed, meaning that you can only travel from a particular vertex to its destination, 
not the other way around (unless the destination vertex itself has an outbound edge to the original vertex).

Also note that this graph may contain self-loops.
A self-loop is an edge that has the same destination and origin; in other words, 
it's an edge that connects a vertex to itself. For the purpose of this question, a self-loop is considered a cycle.

For a more detailed explanation, please refer to the Conceptual Overview section of this question's video explanation.
"""

# Whats the input? The input is an adjacency list
# Whats the output? A boolean indicating whether a cycle exists in the graph or not

# 💡 Sample Adjacency List
"""
edges = [
    [1, 3],
    [2, 3, 4],
    [0],
    [],
    [2, 5],
    [],
]
"""

# Sample Output here: Should be true.
"""
pThere are multiple cycles in this graph:
1) 0 -> 1 -> 2 -> 0
2) 0 -> 1 -> 4 -> 2 -> 0
3) 1 -> 2 -> 0 -> 1
These are just 3 examples; there are more.
"""

# An adjcaceny list is a way we can represent graphs in our computers.
# Hmm, How do we approach this problem?

# When building an adjacency list in Python; We often use the default dict.

# First thing lets see whether I understand the concept of defaultdict.
from collections import defaultdict
# Say we have a list of tuples.
lord_of_rings = [('Frodo', 'Baggins'), ('Pippin', 'Took'), ('Andy', 'Serkiss'), ('Frodo', 'Aaragon'), ('Andy', 'Sander'), ('Frodo', 'Blessing')]
list_dictionary = defaultdict(list)

for name, surname in lord_of_rings:
    list_dictionary[name].append(surname)

print('Here is my list dictionary:', list_dictionary)

# What if we wanted to play with integers and strings?
str_default_dict = defaultdict(str)
int_default_dict = defaultdict(int)

str_for_friday = 'missisipi'
for i in str_for_friday:
    int_default_dict[i] += 1

print('Character Occurence in string:',int_default_dict.items())

for i in str_for_friday:
    str_default_dict[i] = i

print(str_default_dict.items())


# CYCLE IN GRAPH
# O(V + E) time and O(V) space

def has_cycle(edges):
    # What is the input? A list of edges
    # What is the output? A Boolean value that indicates whether a cycle exists or not.

    def dfs(node, visited, rec_stack):
        visited[node] = True
        rec_stack[node] = True
        
        for neighbor in edges[node]:
            if not visited[neighbor]:
                if dfs(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True
        
        rec_stack[node] = False
        return False
    
    num_nodes = len(edges)
    # This marks whether the current node is visted or not
    visited = [False] * num_nodes
    # Fills the value if its a true or face
    rec_stack = [False] * num_nodes
    
    for node in range(num_nodes):
        print(node)
        if not visited[node]:
            if dfs(node, visited, rec_stack):
                return True
    
    return False

# Sample Input
edges = [[1, 2], [2], [0], [0]]
edges1 = [
    [1, 3],
    [2, 3, 4],
    [0],
    [],
    [2, 5],
    [],
]
print('Hello world!')
print(has_cycle(edges1))  # Output: True

# Prints from 0 to 4
# for i in range(5):
#     print(i)
