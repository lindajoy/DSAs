"""
💡 House Robber II

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed. All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.
"""

# Whats the input? An array of houses, values reprsendt the money stashed in each house.
# Whats the output? The maximum amount of profit that one can get.

# Question for the interviewer:
# 1. Can we assume that we will always receive valid inputs?
# 2. Our houses array will always contain positive integers right?

def house_robber_2(houses):
    if len(houses) == 2 or len(houses) == 3:
        return max(houses)
    
    def helper(houses):
        rob1, rob2  = 0, 0

        for n in houses:
            temp = max(rob1 + n , rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    
    return max(houses[0], helper(houses[1:]), helper(houses[:-1]))

print(house_robber_2([1,2,3,1]))

# Another thought I had was: We dont need to look for the max of houses at index 0
def house_robber(houses):
    if len(houses) == 2 or len(houses) == 3:
        return max(houses)
    
    if len(houses) == 1:
        return houses[0]
    
    def helper(houses):
        rob1, rob2  = 0, 0

        for n in houses:
            temp = max(rob1 + n , rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    
    return max(helper(houses[1:]), helper(houses[:-1]))

print(house_robber_2([1,2,3,1]))

