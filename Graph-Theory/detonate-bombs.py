"""
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. 
This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri].
 xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. 
These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

TIP: THIS IS A GRAPH THEORY QUESTION: BREADTH FIRST SEARCH OR DEPTH FIRST SEARCH ARE BOTH APPLICABLE ON THIS SOLUTION.

Bombs: Here you are given the list of bombs
"""

import math
from collections import defaultdict

def detonateMaximumBombs(bombs):
    # Create an adjacency list: Creating a graph on our own
    adjList = defaultdict(list)

    # Loop through the list of bombs
    for i in range(len(bombs)):
        for r in range(i + 1, len(bombs)):

            xi, yi, ri = bombs[i]
            xj, yj, rj = bombs[r]

            distance = math.sqrt((xi - xj) ** 2 + (yi -yj) ** 2)

            # Not understood this bit
            if distance <= ri:
                adjList[i].append[r]
            if distance <= rj:
                adjList[r].append[i]

    def dfs(i, visit):
        if i in visit:
            return 
        
        for neighbour in adjList[i]:
            dfs(neighbour,visit)

        return len(visit)

    res = 0
    for i in range(bombs):
        dfs(i, set())
        res = max(res, dfs(i, set))
        return res
