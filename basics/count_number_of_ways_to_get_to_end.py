"""
In this problem you are to count the number of ways of starting at the top-left comer of a2D array and getting to the bottom-right comer.
All moves must either go right or down. For example, we show three ways in a 5 x 5 2D array

Write a program that counts how many ways you can go from the top-left to the bottom-right in a 2D array.

Intuition:

"""

# Takes in the number of rows and columns.
def number_of_ways_to_get_to_end(grid):
    x, y = len(grid), len(grid[0])

    def compute_number_of_ways(n, m):
        if n == m == 0:
            return 1
        
        if number_of_ways[n][m] == 0:
            ways_up =  0 if n == 0 else compute_number_of_ways(n-1, m)
            ways_left =  0 if m == 0 else compute_number_of_ways(n, m - 1)
            number_of_ways[n][m] = ways_left + ways_up
        return number_of_ways[n][m]
        
    number_of_ways = [[0] * y for _ in range(x)]
    return compute_number_of_ways(x-1, y-1)
    
grid = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

print(number_of_ways_to_get_to_end(grid))

