"""
Minimum cost
"""

from ast import List


def minCost(colors, neededTime) -> int:
        left = 0
        right = left + 1
        res = 0

        while right < len(colors):
            if colors[right] == colors[left]:
                res += min(neededTime[right], neededTime[left])
            left += 1
            right += 1

        return res


print(minCost("aaabbbabbbb", [3,5,10,7,5,3,5,5,4,8,1]))
