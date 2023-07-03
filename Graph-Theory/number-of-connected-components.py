"""
Number of Connected Components in an Undirected Graph

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
write a function to find the number of connected components in an undirected graph.

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output: 1

Input: N nodes, List of undirected edges
Output: Number of connected components
"""

def countComponents(n , listofUndirectedEdges):
    # Create an adjacency list to represent a graph
    graph = [[] for _ in range(n)]
    
    print(graph)

    for u,v in listofUndirectedEdges:
        graph[u].append(v)
        graph[v].append(u)

    print("Completed Graph:", graph)

    # Initialize visited array to keep track of the visited nodes
    visited = [False] * n

    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)


    # Perform DFS on each unvisited node
    count = 0

    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1
    return count

n = 5 

edges = [[0, 1], [1, 2], [3, 4]]

print(countComponents(n, edges))