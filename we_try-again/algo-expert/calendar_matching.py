"""
Imagine that you want to schedule a meeting of a certain duration with a co-worker.
You have access to your calendar and your co-worker's calendar (both of which contain your respective meetings for the day,
in the form of [startTime, endTime]), 
as well as both of your daily bounds (i.e., the earliest and latest times at which you're available for meetings every day,
in the form of [earliestTime, latestTime]).

Write a function that takes in your calendar, your daily bounds, your co-worker's calendar, your co-worker's daily bounds, 
and the duration of the meeting that you want to schedule, 
and that returns a list of all the time blocks (in the form of [startTime, endTime]) during which you could schedule the meeting, 
ordered from earliest time block to latest.

Note that times will be given and should be returned in military time. For example: 8:30, 9:01, and 23:56.

Also note that the given calendar times will be sorted by start time in ascending order, as you would expect them to appear in a calendar application like Google Calendar.
"""

calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
dailyBounds1 = ['9:00', '20:00']
calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
dailyBounds2 = ['10:00', '18:30']
meetingDuration = 30

# Here we use the merge intervals algorithm
# Merge the two calendars
# You will have something like: [[10.00, 11.30], [12.00,14.30],[14.30, 15.00], [16.00, 18.00], [18.00, 18.30]]
# Output should be something like:
# (This is the output).
# [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]

# Reminding myself of merge intervals pattern: 
# An interval is a period of time between events or states.
# Random example: That builds up to the solution above:
# Question 1:
# Merge Intervals
"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
"""

# This builds up to the question above.
def merge(intervals):
    intervals.sort(key = lambda x: x[0])

    # We will starting by assuming that the first of our array is the first interval
    res = [intervals[0]]

    for idx in range(1, len(intervals)):
        curr = intervals[idx]
        prev = res[-1]

        # Check for overlap
        if prev[1] < curr[0]:
            res.append(curr)
        else:
            prev[1] = max(prev[1], curr[1])
    return res

# Okay lets head back to the question above:
# I think the pseudocode should be along the lines:
#   1. For the two calendars, we can combine them as a one array(We assume its one person's calendar)
#   2. Using the starting and ending times (per person); what i mean after concatenating the starting should be the max(timePerson1, timePerson2)
#   3. The ending time should be the minimum between the two persons time, so it should be something like min(endingTimePerson1,endingTimePerson2)
#   4. Apply the merge intervals algorithm and find a 30 minute break between the two times.

