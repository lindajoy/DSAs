"""
Write a function that takes in an array of at least three integers and,
without sorting the input array, returns a sorted array of the three largest integers in the input array.

The function should return duplicate integers if necessary; 
for example, it should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12].

array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

Output = [18, 141, 541]

"""

# Breathe, What can you not see

array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
ouput = [18, 141, 541]
arry1 = [541,541,6, 7]
random_list = [23, 56, 11, 89, 45, 32, 7, 98, 17, 62]

# My solution

def find_three_largest_elements(arr):
    # Check for the edge cases or rather the simplest case.
    if len(arr) == 3:
        return arr
    res = []

    while len(res) != 3:
        maximum_val = max(arr)
        res.append(maximum_val)
        arr.remove(maximum_val)
    return res

print(find_three_largest_elements(array))
print(find_three_largest_elements(arry1))
print(find_three_largest_elements(random_list))

def find_largest_three(arr):
    # Say our input is: [541,541,6,7]
    largest = [float('-inf')] * 3
    # [-inf, -inf, -inf]
 
    # Looping through each value in my array.
    # And updating as time goes.
    for num in arr:
        if num > largest[0]:
            largest[2] = largest[1]
            largest[1] = largest[0]
            largest[0] = num
        elif num > largest[1]:
            largest[2] = largest[1]
            largest[1] = num
        elif num > largest[2]:
            largest[2] = num
    return largest

print(find_largest_three(array))

