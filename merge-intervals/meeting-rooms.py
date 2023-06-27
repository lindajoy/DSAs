"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],
return the minimum number of conference rooms required.

Input: intervals = [[9,10],[4,9],[5,17]]
Output: 2

Sorted Version = [[4,9], [5,17], [9,10]]

Start Intervals: [4,5,9]
End Intervals:[9,17,10]

💡 Need to review this again
"""
intervals = [[9,10],[4,9],[5,17]]


def minimumMeetingRooms(intervals):
    startTimes = sorted([i[0] for i in intervals])
    endTimes = sorted([i[1] for i in intervals])
    print(startTimes, endTimes)
    meet_count, curr_count = 0, 0

    # The two pointers
    start, end = 0, 0

    while start < len(intervals):
        if startTimes[start] < endTimes[end]:
            start += 1
            curr_count += 1
        else:
            end += 1
            curr_count -=1

        meet_count = max(meet_count, curr_count)

    return meet_count

print(minimumMeetingRooms(intervals))



