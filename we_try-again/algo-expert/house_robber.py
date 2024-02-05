"""
💡 House Robber

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.
"""

# Brute Force Solution

# We expect an input array of positive integers, right?

def house_robber(houses):
    # Validate the input
    if len(houses) == 0:
        return -1
    
    if len(houses) == 1:
        return houses[0]
    
    if len(houses) ==  2:
        return max(houses)
    

    res = 0

    for i in range(len(houses)):
        for j in range(i+2, len(houses)):
            calculated_sum = houses[j] + houses[i]
            res = max(calculated_sum, res)

    return res

print(house_robber([1,2,3,1]))
# print(house_robber([2,7,9,3,1]))


# Dynamic Programing
def house_robber_dp(houses):
    rob1, rob2 = 0, 0

    for n in houses:
        temp = max(n+rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

print(house_robber_dp([2,7,9,3,1]))
    