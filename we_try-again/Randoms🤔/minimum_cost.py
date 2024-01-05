"""
Minimum Time to Make Rope Colorful.

Alice has n balloons arranged on a rope.
You are given a 0-indexed string colors where colors[i] is the color of the Ith balloon.
Alice wants the rope to be colorful. 
She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. 
You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.
Return the minimum time Bob needs to make the rope colorful.

Example 1:
Input: colors = "abc", neededTime = [1,2,3]
Output: 0

Example 2:
Input: colors = "abaac", neededTime = [1,2,3,4,5]
Output: 3
"""

# This solution did not work
# The reason is I never considered some test input colors and expected output.
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


# print(minCost("aaabbbabbbb", [3,5,10,7,5,3,5,5,4,8,1]))

# What was the ideal solution?
def minCost2(colors, neededTime):
     l = res  = 0

     for r in range(1, len(colors)):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    res += neededTime[l]
                    l = r
                else:
                    res += neededTime[r]
            else:
                l = r
     return res
    #  for r in range(len(colors)):
    #       if colors[l] == colors[r]:
    #            if neededTime[l] < neededTime[r]:
    #                 res += neededTime[l]
    #                 l = r
    #            else:
    #                 res += neededTime[r]
    #       else:
    #            l = r
    #  return res

print(minCost2("aaabbbabbbb", [3,5,10,7,5,3,5,5,4,8,1]))

            
           
