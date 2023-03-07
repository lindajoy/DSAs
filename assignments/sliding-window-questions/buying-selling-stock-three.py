"""
Best Time to Buy and Sell Stock III : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/


You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example: 

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, 
as you are engaging multiple transactions at the same time. 
You must sell before buying again.
"""

class solution:
    def maximumProfitForTwoDays(self, prices:list[int]) -> int:
        # Left represents when you buy , right represents when you sell
        leftPointer, rightPointer = 0, 1
        # Initialize the maximum profit to 0
        maximumProfitlist = []

        while rightPointer < len(prices):
            if(prices[leftPointer] < prices[rightPointer]):
                profit = prices[rightPointer] - prices[leftPointer]
                maximumProfitlist.append(profit)
                leftPointer = rightPointer                
                while (len(maximumProfitlist) > 2):
                   least_Profit =  min(maximumProfitlist)
                   maximumProfitlist.remove(least_Profit)
            else:
                leftPointer = rightPointer
            rightPointer += 1


        return sum(maximumProfitlist)

my_prices = [3,3,5,0,0,3,1,4]
my_prices_2 = [1,2,3,4,5]

x = solution()
print (x.maximumProfitForTwoDays(my_prices))
print(x.maximumProfitForTwoDays(my_prices_2))