"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:
    => The town judge trusts nobody.
    => Everybody (except for the town judge) trusts the town judge.
    => There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] 
representing that the person labeled ai trusts the person labeled bi. 
If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
"""

# Example 1
"""
Input: n = 2, trust = [[1,2]]
Output: 2 
"""

# Incoming = n - 1
# Outgoing = 0

# This a graph problem; Such that we find the incoming and outgoing indices.

from collections import defaultdict

def findJudge(n, trust):
    outgoing = defaultdict(int)
    incoming = defaultdict(int)

    for src, dst in trust:
        outgoing[src] += 1
        incoming[dst] += 1

    for i in range(1, n+1):
        if outgoing[i] == 0 and incoming[i] == n - 1:
            return i
    return -1

print(findJudge(2, [[1,2]]))
print(findJudge(3,[[1,3],[2,3]]))
print(findJudge(3, [[1,3],[2,3],[3,1]]))

