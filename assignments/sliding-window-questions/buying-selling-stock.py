"""
💰 Buying and selling Stock: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock 
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

UNDERSTANDING THE PROBLEM
- Each element in the array represents the price of the stock at a particular time
Iteration: The left index representing when the day starts how much the price of that particular stock is at the time
and by iterating how much you will make.

💡 Approach => Two Pointers approach

PSEUDOCODE
1. Intialize the left and right pointer (Left indicating when you buy the stock while right indicating when you are selling the stock)
2. Initialize the max profit value to 0
2. Loop through the array as long as the right pointer has not surpassed the length of the array.
3. If the left pointer's value is greater than the right pointer value then:
     i) assign the right pointer to the left pointer
     ii) Add the value of the right pointer
  else:
    find the profit by subtracting the right pointer's value from the left pointer's value
    find the maximum profit = max(maxprofit, profit)

The end
"""

class solution:
    def maximumProfit(self, prices:list[int]) -> int:
        # Left represents when you buy , right represents when you sell
        leftPointer, rightPointer = 0, 1
        # Initialize the maximum profit to 0
        maximumProfit = 0

        while rightPointer < len(prices):
            if(prices[leftPointer] < prices[rightPointer]):
                profit = prices[rightPointer] - prices[leftPointer]
                maximumProfit = max(maximumProfit, profit)
            else:
                leftPointer = rightPointer
            rightPointer += 1

        return maximumProfit

my_prices = [7,1,5,3,6,4]
my_2prices = [7,6,4,3,1]

x = solution()
print(x.maximumProfit(my_prices))
print(x.maximumProfit(my_2prices))
