# def min_splits(S):
#     last_occurrence = {}
#     count = 0
#     start = 0

#     for i, char in enumerate(S):
#         if char in last_occurrence and last_occurrence[char] >= start:
#             start = last_occurrence[char] + 1
#             count += 1
#         last_occurrence[char] = i

#     return count + 1

# # Example usage:
# S = "world"
# result = min_splits(S)
# print(result)  # Output: 5

# S = "cycle"
# result = min_splits(S)
# print(result)  # Output: 3


# def max_rook_sum(matrix):
#     max_sum = 0
#     rows = len(matrix)
#     cols = len(matrix[0])

#     for i in range(rows):
#         for j in range(cols):
#             for k in range(i + 1, rows):
#                 for l in range(cols):
#                     if l != j:  # Ensure the rooks are not in the same column
#                         rook_sum = matrix[i][j] + matrix[k][l]
#                         max_sum = max(max_sum, rook_sum)

#     return max_sum

# # Example usage:
# matrix = [
#     [15, 1, 5],
#     [16, 3, 8],
#     [2, 6, 4]
# ]

# print(max_rook_sum(matrix))  # Output will be 16 (placing rooks at (0, 0) and (2, 1))


# def find_maximal_sum(matrix):
#     n = len(matrix)
#     m = len(matrix[0])

#     # Find the maximum element in each row
#     max_row_values = [max(row) for row in matrix]

#     # Find the maximum element in each column
#     max_col_values = [max(matrix[i][j] for i in range(n)) for j in range(m)]

#     # Find the positions of the maximum elements
#     max_row_positions = [row.index(val) for row, val in zip(matrix, max_row_values)]
#     max_col_positions = [col.index(val) for col, val in zip(zip(*matrix), max_col_values)]

#     # Find the two positions with the maximum sum
#     max_sum = 0
#     rook_positions = []

#     for i in range(n):
#         for j in range(m):
#             if i != max_row_positions[i] and j != max_col_positions[j]:
#                 current_sum = matrix[i][j] + matrix[max_row_positions[i]][max_col_positions[j]]
#                 if current_sum > max_sum:
#                     max_sum = current_sum
#                     rook_positions = [(i, j), (max_row_positions[i], max_col_positions[j])]

#     return max_sum, rook_positions

# # Example usage:
# matrix = [
#     [15, 1, 5],
#     [16, 3, 8],
#     [2, 6, 4]
# ]

# max_sum, rook_positions = find_maximal_sum(matrix)
# print(f"Maximal sum: {max_sum}")
# print("Rook positions:", rook_positions)
