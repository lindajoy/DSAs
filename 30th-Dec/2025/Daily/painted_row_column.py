"""
    You are given a 0-indexed array, and an m *n integer matrix mat. 
    arr and mat both contain all the integers in the range [1, m *n].
    
    Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].
    
    Return the smallest index i at which either a row or column will be completely painted in mat.
 """
 
# Two inputs: arr = [1,3,4,2], mat = [[1,4],[2,3]]

# Both contain integers in range [1, (2*2)] => 0 is never contained in the array.

# I think i understand the question now. 

# We are sort of like looping through the array and filling/ painting the matrix.

"""
   Approach
   
   1. Create two arrays rowFreq and colFreq to keep track of the number of filled cells in each row and column respectively.
   2. Create a hashmap to store the position (row and column) of each element in the matrix
   3. Iterate through the array:
        a. For each element, get its position in the matrix from the hashmap.
        b. Increment the corresponding row and column frequencies
        c. If any row frequency equals the number of columns or column frequency equals the number of rows, return the current index.
        
   4. If no complete row or column is found, return -1
"""

"""
  I honestly dont know what is going on this question....🥲
"""
def firstCompleteIndex(arr, mat):
    # rows and columns
    m = len(mat)
    n = len(mat[0])
    
    # Declare array frequency for row and column
    rowFreq = [0] * m
    colFreq = [0] * n
    
    map = {}
    for i in range(m):
        for j in range(n):
            map[mat[i][j]] = [i,j]
            
            
            
    for i in range(len(arr)):
        idx = map[arr[i]]
        c = idx[1]
        r = idx[0]
        
        rowFreq[r] += 1
        colFreq[c] += 1
        
        if rowFreq[r] == n or colFreq == m:
            return i
        
    return -1


