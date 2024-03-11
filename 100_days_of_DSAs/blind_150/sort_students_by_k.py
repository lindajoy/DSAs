"""
SORT THE STUDENTS BY THEIR KTH SCORE.

There is a class with m students and n exams. 
You are given a 0-indexed m x n integer matrix score, 
where each row represents one student and score[i][j] denotes the score the ith student got in the jth exam. 
The matrix score contains distinct integers only.

You are also given an integer k. 
Sort the students (i.e., the rows of the matrix) by their scores in the kth (0-indexed) exam from the highest to the lowest.

Return the matrix after sorting it
"""

# INPUT
score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], 
k = 2

# OUTPUT
Output= [[7,5,11,2],[10,6,9,1],[4,8,3,15]]

# Dont know whats going on.
def sort_students_by_k_th_score(score, k):
    sorted_students = sorted(score, key=lambda x: x[k], reverse=True)
    return sorted_students
