"""
Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
"""
# Example 1
# Input: [[1,2],[2,3],[3,4],[1,3]]
# Expected Otput : 1

# Lets break it down
# We can start by sorting the input:
# Assume that these are meeting rooms... The one at index 1, Overlaps with the one at index 0.
# [ [1, 2], [1, 3], [2, 3], [3, 4] ]

def removeOverlappingIntervals(intervals):
    # We are using the end time.
    # Hmm, does not make sense to me...
    intervals.sort(key = lambda x: x[1])

    # Initialize an empty stack; Ideally its a list.
    stack = []

    # Loop through each interval in intervals.
    for interval in intervals:
        # check overlap, if yes ignore
        if stack and interval[0] < stack[-1][1]:
            continue
        stack.append(interval)
        # First iteration: stack will have : [[1,2]]
    return len(intervals) - len(stack)

print(removeOverlappingIntervals([[1,2],[2,3],[3,4],[1,3]]))