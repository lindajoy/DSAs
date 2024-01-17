"""
💡 SPIRAL TRAVERSE

Write a function that takes in an n x m two-dimensional array 
(that can be square-shaped when n == m) and 
returns a one-dimensional array of all the array's elements in spiral order.

Spiral order starts at the top left corner of the two-dimensional array, 
goes to the right, and proceeds in a spiral pattern all the way until every element has been visited.

Sample Input = [
            [1,   2,  3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10,  9,  8, 7],
]
Sample Output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# 💡 Hmm having trouble understanding what is spiral_traverse..🤔
"""
def spiral_order(matrix):
    result = []

    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                print("Here is my row", row)
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result


Input = [
        [1,   2,  3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10,  9,  8, 7],
]
print(spiral_order(Input))