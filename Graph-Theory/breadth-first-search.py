"""
Breadth First Search.

The BFS algorithm is used to search a tree or graph data structure for a node that meets a certain criteria.

It starts at the root of the graph,and searches/visits all the nodes at the current depth before moving to the next depth.

The only catch here is, that, unlike trees, graphs may contain cycles, so we may come to the same node again. 
To avoid processing a node more than once, we divide the vertices into two categories: Visited and Not visited.

A boolean visited array is used to mark the visited vertices.

For simplicity its assumed that all vertices are reachable from the starting vertex.

BFS uses a queue data structure for traversal.

Basic Pseudocode:

1. Declare a queue and insert the starting vertex
2. Initialize a visited array and mark the starting vertex as visited.
3. Follow the below process till the queue becomes empty:
    i) Remove the first vertex of the queue
    ii) Mark that first vertex as visited
    iii) Insert all the unvisted neighbors of the vertex into the qeue.

Link: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
"""

from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)


    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True


        while queue:
            s = queue.pop(0)
            print(s, end= "")


            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        