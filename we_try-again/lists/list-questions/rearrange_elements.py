"""
Implement a function rearrange(lst) 
which rearranges the elements such that all the negative 
elements appear on the left and positive elements appear
 at the right of the list. Note that it is not necessary to maintain the sorted order of the input list.

Generally zero is NOT positive or negative, 
we will treat zero as a positive integer for this challenge!
So, zero will be placed at the right.

Input 
[10,-1,20,4,5,-9,-6]

Output:
[-1,-9,-6,10,20,4,5]
"""
k = [10,-1,20,4,5,-9,-6]

def sortNegativeAndPositive(lst):
    negative, positive  = [], []

    for i in lst:
        if i < 0:
            negative.append(i)
        else:
            positive.append(i)
    return negative + positive

print(sortNegativeAndPositive(k))
print(sortNegativeAndPositive([300, -1, 3, 0]))
print(sortNegativeAndPositive([0, 0, 0, -2]))