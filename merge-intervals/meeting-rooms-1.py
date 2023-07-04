"""
Given the array of meeting time intervals, 
where each interval consists of a pair of starting times and an ending times, 
you need to identify whether a person can attend all meetings or not.
"""
intervals = [[1, 3], [4, 6], [5, 8], [7, 9]]

def meeting_rooms(intervals):

    start = intervals[0][0]
    end = intervals[0][1]

    for i in intervals[1:]:
        if i[0] < end:
            return False
        else:
            start = i[0]
            end = i[1]

    return True


