"""
💡 List Comprehensions
"""
"""
EXAMPLE 1

This is a normal function that loops over the range of the numbers in the list and returns the square of each number
squares = []

for i in range(10):
    squares.append(i * i)
"""
# Example 1 -> Implemented as list comprehension

squares = [i * i for i in range(10)]
squares

# Example 2 -> List Comprehension 2
txns = [1.09, 23.56, 56.86, 4.56, 6.78]
TAX_RATE = .08

def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)

final_prices = [get_price_with_tax(i) for i in txns]
print(final_prices)