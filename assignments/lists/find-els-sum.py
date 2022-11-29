'''
In this problem, you have to implement the find_sum(lst,k) 
function which will take a number k as input and return two numbers that add up to k.

Sample Input

lst = [1,21,3,14,5,60,7,6]
k = 81

Sample Output

lst = [21,60]

'''

def find_sum(lst, k):
    # Initializes an empty dictionary
    seen = {}

    # Loops through the list
    for el in lst:
        diff = k - el
        if seen.get(el):
            return [el, diff]
        seen[diff] = el
    
lst = [1,21,3,14,5,60,7,6,77]
k = 81

find_sum(lst,k)

'''
💡 Brute Force Algorithm
Traversing through the whole array of size, for each element in the list, check if any elements add up to the target k.

Since we are iterating through the whole array , n times in the worst case,
therefore time complexity is O(n2)
'''

def find_sum_brute(list, k):
    for i in range(len(list)):
        for j in range(len(list)):
            if(list[i]+list[j] is k and i is not j):
                return [list[i],list[j]]

print(find_sum_brute(lst,k))

print(len(lst))
print(len(lst) - 1)

print('Hmm interesting')

def binary_search(a, item):
    left, right = 0, len(a) - 1
    found = False
    indexi = -1

    while left <= right and not found:
        # Find the median value => Use floor division to return a significant whole number.
        mid =  left + right // 2
        
        if a[mid] == item:
           indexi = mid
           found = True

        else:
            if item < a[mid]:
                right = mid - 1

            else:
                left = mid + 1

    if found:
        return indexi

    else:
        return -1

def find_sum3(list,k):
    list.sort()
    for j in range(len(list)):
        
        # find the difference in list through binary search
        # return the only if we find an index
        index = binary_search(lst, k -lst[j])
        if index is not -1 and index is not j:
            return [lst[j], k -lst[j]]

print(find_sum3([1, 5, 3], 2))
print(find_sum3([1, 2, 3, 4], 5))