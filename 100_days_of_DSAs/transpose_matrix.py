"""
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.


"""
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]


def transpose_matrix(matrix):
    ROWS, COLUMNS = len(matrix), len(matrix[0])
    for r in range(ROWS):
            print(matrix[r][0])
            print(matrix[r][1])
            print(matrix[r][2])


print(transpose_matrix(matrix))