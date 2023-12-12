"""
Your input is an array of integers, and you have to reorder its entries so that the even entries appear first. 
"""
"""
Example 1:

Input: [3, 8, 12, 5, 6, 10]
Output: [8, 12, 6, 10, 3, 5]
"""
Input =  [3, 8, 12, 5, 6, 10]

def even_odd(lst):
    next_even, next_odd = 0, len(lst) - 1

    while next_even < next_odd:
        if lst[next_even] % 2 == 0:
            next_even += 1
        else:
            lst[next_even], lst[next_odd] = lst[next_odd],lst[next_even]
            next_odd -= 1
    return lst

print(even_odd(Input))
