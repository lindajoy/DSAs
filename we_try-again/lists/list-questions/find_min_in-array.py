"""
Implement a function findMinimum(lst) which finds the smallest number in the given list.

A list of integers: [9,2,3,6]

Sample Input: [9,2,3,6]

Output: 2
"""
my_list = [9,2,3,6]
'''
My first thought was using the sort function and taking the first element at index[0], however this is not advisable in
a real interview(But I think you should ask) 🤔
'''
# 💡 First Implementation
def findSmallestInteger(lst):
    if len(lst) == 0:
        return None
    sorted_list = sorted(lst)
    print(sorted_list[0])
    return sorted_list[0]

print(findSmallestInteger([100, 12, 34, 40]))

# 💡 Second Implementation
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