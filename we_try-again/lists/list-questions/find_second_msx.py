"""
Implement a function find_second_maximum(lst) which returns the second largest element in the list.
"""
lst = [9,2,3,6]

# This should be the output
# output = 6

# This solution does not work well.

def find_second_maximum(lst):
    # Think about the edge cases first
    if len(lst) == 1 or len(lst) == 0:
        return None
    # first we work with the assumption that the large, and second large integers
    # are in the first two indexes

    large, second_large = lst[0], lst[1]
    temporary_int = 0
    temp_set = set(lst)
    temp_list = list(temp_set)
    print(temp_list)

    for i in range(len(lst)):
       if temp_list[i] > large and temp_list[i] > second_large:
           temporary_int = large
           large = temp_list[i]

       if temporary_int > second_large:
           second_large = temporary_int

       elif temp_list[i] > second_large:
           second_large = temp_list[i]
    
    
    return second_large
           
           

# print(find_second_maximum(lst))
# print(find_second_maximum([4, 2, 1, 5, 0]))
# print(find_second_maximum([8, 8, 8, 8, 4, 4, 4, 4]))

# 💡 Second implementation(Works better) 
# PSEUDOCODE:
#   1. Get rid of the edge cases, that means that you need to check whether the list has enough elements to loop over
#   2. Initialize the large and the second largest to the element at zero index, Also intialize a set
#      REASON: Sets do not allow duplicate values, So we are getting rid of the chance where our second large and large element might be equal
#       CONSIDER INPUT: 8, 8, 8, 8, 4, 4, 4, 4
#   3. Loop over the list:
#       i) Check if x and y are equal if they are assign value el to y
#       ii) if el is greater than y , then assign el to y
#       iii) if y is greater than x then you need to swap them
#
# Key takeaway:  Sets' elements are not modifiable, however the set itself is modifiable 🤯

def find_scd_max(lst):
    # We get rid of the edge cases first.
    if len(lst) == 1 or len(lst) == 0:
        return None
    
    # We add the first elements as our place holder
    x, y = lst[0], lst[0]
    seen = set()

    for el in lst:
        if x == y:
            y = el
        if el in seen:
            continue
        if el > y:
            y = el
        if y > x:
            x, y = y,x
        seen.add(el)
    return y

print(find_scd_max([8, 8, 8, 8, 4, 4, 4, 4]))
print(find_scd_max([4, 2, 1, 5, 0]))

# 💡 Solution 3: Traversing the list twice.
# Pseudocode:
# 1. Initialize first_max and second_max to infinity
# 2. Loop through the list to initialize the first_max
# 3. Loop through the list again initialize the second_max
# The time complexity here is O(N)2 => QUADRATIC COMPLEXITY because we have two loops; Traverse the 
# List twice.

def find_scd_max3(lst):
    # Ensure the inital value is set to -inf
    first_max = float('-inf')
    sec_max = float('-inf')

    for item in lst:
        if item > first_max:
            first_max = item

    # find second max
    for item in lst:
        if item != first_max and item > sec_max:
            sec_max = item
    return sec_max

print('Another method:', find_scd_max3( [8, 8, 8, 8, 4, 4, 4, 4]))