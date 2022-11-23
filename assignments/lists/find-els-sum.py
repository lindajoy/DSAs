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
    
lst = [1,21,3,14,5,60,7,6]
k = 81

find_sum(lst,k)

'''
💡 Brute Force Algorithm
'''

def find_sum_brute(list, k):
    for i in range(len(list)):
        for j in range(len(list)):
            if(list[i]+list[j] is k and i is not j):
                return [list[i],list[j]]

print(find_sum_brute(lst,k))
