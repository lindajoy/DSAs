"""
We are given an array of closed intervals, intervals, where each interval has a start time and an end time. 
The input array is sorted with respect to the start times of each interval. For example, intervals = [ [1,4], [3,6], [7,9] ]
is sorted in terms of start times 1, 3 and 7.
Your task is to merge the overlapping intervals and return a new output array consisting of only the non-overlapping intervals.
"""
intervals = [[1,5], [3,7],[4,6],[6,8]]

print('The first element is:',[intervals[0]])

# Hint: Combine all  of the overlappping intervals.

# Expected Output in this case is: [[1,8]]

def merge_intervals(intervals):

    # We start with the edge cases first; Which in this case is
    # If the intervals has a length of one or no intervals at all.
    # We are sort of ensuring that our intervals has something.

    if not intervals:
        return []
    
    merged = [intervals[0]]

    for interval in [intervals[1:]]:
        print('Intervals:',interval[0][0])
        print('Intervals:',interval[0][1])

        print(merged[][1])
        print('Here the interval:',interval[0][0])

        if interval[0][0] < merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[0][1])
        else:
            merged.append(interval)

    return merged


'''
Given this input: [1,5], [3,7],[4,6],[6,8]
Expected Output Here will be: [[1,8]]
'''

# print(merge_intervals(intervals))

"""
💡 Retried 2
"""


def merge_intervals2(intervals):
    if not intervals:
        return []

    merged = [intervals[0]]
    for interval in intervals[1:]:
        print(interval[0])

        if interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)

    return merged

print(merge_intervals2(intervals))
