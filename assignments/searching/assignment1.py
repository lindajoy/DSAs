"""
Given an integer return the index that matches the integer given.

if the integer does not exist return -1
[1,5,3,2,2,1,7,6]


Pseudocode:
   1. Loop/ iterate over the array to find the matching element.
   2. If an the index in the array returns a matching element return the index of the array.
   3. If not found, return -1
   
Edge cases:
   1. What if the integer in question is duplicated?

Time complexity of the solution: O(N)
Space complexity of the solution: O(1)
"""

def search_integer(array ,int):
    for i in range(len(array)):
        if array[i] == int:
            return i
    return -1
        


unsorted_arry2 = [1, 1, 2, 3, 5, 6]
result = search_integer(unsorted_arry2, 1)
print(result)


'''
💡 Second solution
   Using binary trees:
   With binary trees the time complexity is logarithimic time complexity(O)
'''
integer = 9
def binary_search1(A):
    Left, Right  = 0, len(A) -1

    while Left <= Right:
        # Get the medium element in the array
        medium = Left + (Right - Left) // 2

        if A[medium] < integer:
            Left = medium + 1
        elif A[medium] == integer:
            return medium
        else:
            Right = medium - 1

    return -1

unsorted_arry3 = [0,1,2,3,5]
result2 = binary_search1(unsorted_arry2)
print(result2)



       



