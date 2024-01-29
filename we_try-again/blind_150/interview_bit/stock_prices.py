"""
Variation of best time to buy and sell stock.

Write an efficient function that takes stock_prices and returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.
"""
stock_prices = [10, 7, 5, 8, 11, 9]

# Maximum profit will be achieved when an individual buys stock at 5 and sells at 11
# This algorithm takes O(N) considering that we are traversing through the entire array.
# A space complexity of O(1).

def get_max_profit(stocks):
    # You always forget about validating your input.
    # What if the stocks are empty or an empty list?
    if len(stocks) < 2 or not stocks:
        return 0
    
    left, right = 0, 1
    max_profit = 0

    while right < len(stocks):
        if stocks[left] < stocks[right]:
            profit = stocks[right] - stocks[left]
            max_profit = max(max_profit, profit)
            right +=1
        elif stocks[left] > stocks[right]:
            right += 1
            left += 1
    return max_profit

print(get_max_profit([10, 7, 5, 8, 11, 9]))

# Time Complexity of this solution is O(N)2
# Using the enumerate function. Hmm, I dont like this approach but I thought I could learn from it
def get_max_profit2(stock_prices):
    maxProfit = 0

    for earlier_time, earlier_price in enumerate(stock_prices):
        for later_time in range(earlier_time + 1, len(stock_prices)):
            later_price = stock_prices[later_time]
            potential_profit = later_price - earlier_price
            maxProfit = max(maxProfit, potential_profit)
    return maxProfit

print(get_max_profit2([10, 7, 5, 8, 11, 9]))
