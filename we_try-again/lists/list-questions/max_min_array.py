"""
Implement a function called max_min(lst) which will re-arrange the elements of a sorted list
such that the 0th index will have the largest number, the 1st index will have the smallest, 
and the 2nd index will have second-largest, and so on. 
In other words, all the even-numbered indices will have the largest numbers in the list in descending order 
and the odd-numbered indices will have the smallest numbers in ascending order.

Input: Sorted List
Output: A list with elements stored in max/min form

Sample Input: lst = [1,2,3,4,5]
Sample Output: lst = [5,1,4,2,3]
"""

def max_minimum(lst):
    # Initialize an empty list
    max_min = []
    while len(lst):
        max_min.append(lst[-1])
        lst.pop(-1)
        if len(lst)> 0:
            max_min.append(lst[0])
            lst.pop(0)
    return max_min

print(max_minimum([1,2,3,4,5]))

