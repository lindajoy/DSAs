"""
Implement a function findMinimum(lst) which finds the smallest number in the given list.

A list of integers: [9,2,3,6]

Sample Input: [9,2,3,6]

Output: 2
"""
my_list = [9,2,3,6]

def smallestIntegerInList(lst):
    if len(lst) == 0:
        return None
    
    result = lst[0]
    for i in lst:
        if result >= i:
            result = i

    return result

print(smallestIntegerInList(my_list))
print(smallestIntegerInList([100, 12, 34, 40]))
print(smallestIntegerInList([4, 5, 0, 3, 6]))