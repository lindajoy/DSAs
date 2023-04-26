"""
Suppose you have the list of weights and corresponding values for n items. You have a knapsack that can carry a specific amount of weight at a time called capacity.

You need to find the maximum profit of items using the sum of values of the items you can carry in a knapsack. 
The sum of the weights of the items should be less than or equal to the knapsack’s capacity.

If any combination can’t make the given knapsack capacity of weights, then return 0

Inputs: Capacity, Weights and Values

Ref:https://www.educative.io/courses/grokking-coding-interview-patterns-python/m2L004ZMl2O
"""

def find_max_knapsack(weights, values, capacity):
    # Remove the edge cases first
    if capacity <= 0 or len(values) != len(weights) or len(values) == 0:
        return 0

    # Initialize an empty profits array
    profits = [0] * (capacity + 1)

    # Iterate through the values of the array => Since they are the same.
    for i in range(len(values)):
        # This means that you are looping through the array in reverse.
        for c in range(capacity, -1, -1):
            print('Heres the first value of I', i)
            if weights[i] <= c:
                # Saving the profit for printing purposes
                new_profit = profits[c - weights[i]] + values[i]
                profits[c] = max(profits[c], new_profit)
                
        return profits[capacity]


weights = [1, 2, 3, 5]
values = [1, 5, 4, 8]
capacity = 6

print(find_max_knapsack(weights,values, capacity))



