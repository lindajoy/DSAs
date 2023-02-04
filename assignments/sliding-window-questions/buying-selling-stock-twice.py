"""
💡 Best Time to Buy and Sell Stock II: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock.
You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

PSEUDOCODE
1. Intialize the left and right pointer (Left indicating when you buy the stock while right indicating when you are selling the stock)
2. Initialize the max profit value to 0
2. Loop through the array as long as the right pointer has not surpassed the length of the array.
3. If the left pointer's value is greater than the right pointer value then:
     i) assign the right pointer to the left pointer
     ii) Add the value of the right pointer
  else:
    i) find the profit by subtracting the right pointer's value from the left pointer's value
    ii) find the maximum profit = max(maxprofit, profit)
    iii) assign the right pointer to the left pointer


The end

"""

class solution:
    def maximumProfitForDiffDays(self, prices:list[int]) -> int:
        # Left represents when you buy , right represents when you sell
        leftPointer, rightPointer = 0, 1
        # Initialize the maximum profit to 0
        maximumProfitlist = []

        while rightPointer < len(prices):
            if(prices[leftPointer] < prices[rightPointer]):
                profit = prices[rightPointer] - prices[leftPointer]
                maximumProfitlist.append(profit)
                leftPointer = rightPointer                
            else:
                leftPointer = rightPointer
            rightPointer += 1


        return sum(maximumProfitlist)

my_prices = [7,1,5,3,6,4]
my_prices_2 = [1,2,3,4,5]
my_3prices = [7,6,4,3,1]

x = solution()
print(x.maximumProfitForDiffDays(my_prices))
print(x.maximumProfitForDiffDays(my_prices_2))
print(x.maximumProfitForDiffDays(my_3prices))

