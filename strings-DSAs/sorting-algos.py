"""
sort your array such thet the even numbers come first then the odd
"""


def even_odd(A):
    next_even , next_odd = 0 , len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1
    return A

sample_array = [2,4,7,9,3,3,4]
print(even_odd(sample_array))