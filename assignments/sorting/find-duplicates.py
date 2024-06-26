"""
Find duplicates in the arry 

This solution has a time complexity of O(n)2 => Quadratic Complexity

Space Complexity is O(1)

Another way would be create a hashset if the number appears twice, return
the number but the issue here is that it uses extra space which we dont want.

Here's the link to question on leetcode: https://leetcode.com/problems/find-the-duplicate-number/
"""

def findDuplicates(arry):
    for i in range(len(arry)):
        for j in range(i+1, len(arry)):
            if arry[i] == arry[j]:
                return arry[i]

x = [1,3,4,2,2]
# print(findDuplicates(x))

"""
Floyd's Hare and Tortoise Algorithm
"""

def findDuplicates2(array):
    slow, fast = 0,0

    while True:
        slow = array[slow]
        fast = array[array[fast]]
        if fast == slow:
            break

        slow = array[0]
        while slow != fast:
            slow = array[slow]
            fast = array[fast]
            

        return slow

print(findDuplicates2(x))
