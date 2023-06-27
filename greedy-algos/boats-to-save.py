"""
You are given an array people where people[i] is the weight of the ith person, 
and an infinite number of boats where each boat can carry a maximum weight of limit.


Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

Input: people = [3,2,2,1], limit = 3
[1,1,1,3]
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
"""
people = [3,2,2,1]
[1,2,2,3]
3
limit = 3
def minimumNumberofBoats(boats, limit):
    boats_sorted = sorted(boats)
    print(boats_sorted)
    left, right = 0, len(boats) - 1
    count = 0

    while left < len(boats_sorted):
        if left == right:
            count += 1
            return count
        
        if boats_sorted[left] + boats_sorted[right] == limit:
            count += 1
            left += 1
            right -= 1

        elif boats_sorted[left] + boats_sorted[right] > limit:
             count += 1
             right -= 1


    return count


print(minimumNumberofBoats(people, limit))
