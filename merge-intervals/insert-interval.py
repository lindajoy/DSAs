"""
You are given an array of non-overlapping intervals intervals
 where intervals[i] = [starti, endi] represent the start and the end of the ith interval 
 and intervals is sorted in ascending order by starti. 
 You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
"""
"""
This code below is buggy because my while loop is not terminating.
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

        for interval in arr[1:]:

            if interval[0] <= start_element[-1][1]:
                start_element[-1][1] = max(start_element[-1][1], interval[1])
            else:
                start_element.append(interval)

    return start_element

print(insertInterval(new_interval, existing_intervals))