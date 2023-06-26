"""
Imagine that you want to schedule a meeting of a certain duration with a co-worker. 
You have access to your calendar and your co-worker's calendar (both of which contain your respective meetings for the day, 
in the form of [startTime, endTime]), as well as both of your daily bounds
(i.e., the earliest and latest times at which you're available for meetings every day, in the form of [earliestTime, latestTime]).

Write a function that takes in your calendar, your daily bounds, your co-worker's calendar, 
your co-worker's daily bounds, and the duration of the meeting that you want to schedule, 
and that returns a list of all the time blocks (in the form of [startTime, endTime]) during which you could schedule the meeting, 
ordered from earliest time block to latest.

Note that times will be given and should be returned in military time. For example: 8:30, 9:01, and 23:56.

Also note that the given calendar times will be sorted by start time in ascending order, 
as you would expect them to appear in a calendar application like Google Calendar.
"""

"""
Sample Input:

calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
dailyBounds1 = ['9:00', '20:00']
calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
dailyBounds2 = ['10:00', '18:30']
meetingDuration = 30

Sample Output:

[['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]
"""

"""
💡 Pattern => Merge Intervals

Pseudocode:
STEP 1: Merge the two calendars together and sort by the start time.
"""
"""
Lesson 1: List concatenation
l1 = [1,4,6,8]
l2 = [2,3,7]
x = l1 + l2
=> Output [1, 4, 6, 8, 2, 3, 7]
x.sort()
=> Output [1, 2, 3, 4, 6, 7, 8]
print(x)
"""

"""
Disclaimer: Does not solve the problem yet
"""

calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
dailyBounds1 = ['9:00', '20:00']
calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
dailyBounds2 = ['10:00', '18:30']
meetingDuration = 30

def calendarMatching(daily_Bounds_1, calendar_1, co_worker_bounds, co_worker_calendar, duration_of_meeting):

    # Merged durations
    booked_time = calendar_1 + co_worker_calendar
    merged = []
    freeTime = []

    
    # Helper function that helps in sorting the array
    def get_start_time(interval):
        x = interval[0].split(':')
        return int(x[0])
    
    booked_time.sort(key = lambda x: get_start_time(x)) 

    def mergeIntervals():
        current_start = booked_time[0][0]
        current_end = booked_time[0][1]

        for interval in booked_time[1:]:
            if interval[0] < current_end:
                current_end = max(current_end,interval[1])
            else:
                merged.append([current_start, current_end])
                current_start = interval[0]
                current_end = interval[1]

        merged.append([current_start, current_end])
        return merged
    
    merged = mergeIntervals() 
    print('😌',merged)  # [['9:00', '11:30'], ['12:00', '14:30'], ['14:30', '15:00'], ['16:00', '18:00']]

    def subtract_time(interval):
        time = interval.split(':')
        hour = (time[0])
        print(int(hour))
        minutes = 60 * int(hour)

        return abs(minutes + int(time[1]))

    print(merged)
    for i in range(len(merged)):

        for j in range(1, len(merged)):

            if subtract_time(merged[j][0]) >= (subtract_time(merged[i][1])):

                if subtract_time(merged[j][0]) - (subtract_time(merged[i][1])) >= duration_of_meeting:
                    freeTime.append([merged[i][1], merged[j][0]])

    return freeTime
   
    # # Do a typical Merge Interval
    # merged = []
    # current_start = max(daily_Bounds_1[0], co_worker_bounds[0])
    # current_end = booked_time[0][1]

    # for interval in booked_time:
    #     if subtract_time(interval[0]) >= subtract_time(current_end):
    #         if subtract_time(interval[0]) - subtract_time(current_end) >= duration_of_meeting:
    #             merged.append([current_end, interval[0]])
    #             current_start = max(interval[1], daily_Bounds_1[0], co_worker_bounds[0])
    #         current_end = max(current_end, interval[1])
        
    #     if subtract_time(current_end) < min(subtract_time(daily_Bounds_1[1]), subtract_time(co_worker_bounds[1])) and subtract_time(current_end)- subtract_time(current_start) >= duration_of_meeting:
    #         merged.append([current_end, min(daily_Bounds_1[1], co_worker_bounds[1])])

    # return merged

print(calendarMatching(dailyBounds1, calendar1, dailyBounds2, calendar2, meetingDuration))



    

