"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
"""

# Lets break down the problem:

def numberOfmeetingRooms(intervals):
    # Check if the input exists.
    # Proud of you! You remembered to validate the inputs.
    # Does the intervals array/ list have something in it? 🤔
    if len(intervals) == 0:
        return 0
    
    # We get the starting times.
    startTimes = sorted([interval[0] for interval in intervals])
    print('Starting Times 🤔', startTimes)
    # We get the ending times.
    # At this point we have: [4, 5, 9]
    endTimes = sorted([interval[1] for interval in intervals])
    print('Ending Times 🤔', endTimes)
    # At this point we have : [9, 10, 17]

    meet_count, curr_count = 0, 0
    s_ptr, e_ptr = 0, 0
    # Loop through the entire array while s_ptr is less than the length of the intervals.
    # Fun fact I see that these questions build up to solve the bigger question here: (like the calendar matching)
    while s_ptr < len(intervals):
        if startTimes[s_ptr] < endTimes[e_ptr]:
            s_ptr += 1
            curr_count += 1
        else:
            e_ptr += 1
            curr_count -= 1
        meet_count = max(meet_count, curr_count)
    return meet_count


print(numberOfmeetingRooms([[9,10],[4,9],[5,17]]))
