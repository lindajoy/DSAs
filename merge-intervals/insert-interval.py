"""
You are given an array of non-overlapping intervals intervals
 where intervals[i] = [starti, endi] represent the start and the end of the ith interval 
 and intervals is sorted in ascending order by starti. 
 You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
"""
"""
🐛 This code below is buggy because my while loop is not terminating.
"""
existing_intervals = [[1,3],[4,5],[7,8],[9,12],[13,14]]

new_interval = [2,10]

def insertInterval(interval, arr):
    isInserted = False

    for i in range(len(arr)):
        if interval[0] < arr[i][1]:
            arr[i][1] = max(arr[i][1], interval[1])
            isInserted = True
            break
        else:
            i.append(interval)
            isInserted = True
            

    while isInserted:
    
        start_element = [arr[0]]
        isInserted = False  # Update isInserted to False at the beginning of the while loop


        for interval in arr[1:]:

            if interval[0] <= start_element[-1][1]:
                start_element[-1][1] = max(start_element[-1][1], interval[1])
            else:
                start_element.append(interval)

    return start_element



def insertInterval2(interval, newInterval):
    start, end = newInterval[0], newInterval[1]
    n = len(interval)
    idx = 0

    # Find the place where it will be inserted
    while idx < n and start > interval[idx][1]:
        idx += 1
    i = idx

    # Keep finding and updating the start and end if they overlap
    while (i < n ) and (start < interval[i][1]) and interval[i][0] <= end:
        start = min(start, interval[i][0])
        end = max(end, interval[i][1])
        i+= 1

    return interval[:idx] + [[start, end]] + interval[i:]

print(insertInterval2(existing_intervals, new_interval))