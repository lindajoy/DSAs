"""
Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
"""

intervals = [[1,2],[2,3],[3,4],[1,3]]
i2 = [[1, 3], [3, 4], [4, 6], [5, 8], [6, 9], [9, 11], [10, 12], [11, 13]]
i3 = [[3, 5], [5, 6], [7, 10], [10, 11], [13, 15], [15, 16]]

def nonoverlapping(intervals):
    end = intervals[0][1]
    start = intervals[0][0]


    count = 0
    
    # Loop through the entire array:

    for i in intervals[1:]:
        print('Here is the interval:', i[0])
        if i[0] < end:
            count += 1
            intervals.remove(i)

        else:
            end = i[1]
            start = i[0]


    return count

print(nonoverlapping(intervals))
print(nonoverlapping(i2))
print(nonoverlapping(i3))

    

