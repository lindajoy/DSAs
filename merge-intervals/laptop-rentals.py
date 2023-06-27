"""
You're given a list of time intervals during which students at a school need a laptop. 
These time intervals are represented by pairs of integers [start, end], where 0 <= start < end.
 However, start and end don't represent real times; therefore, they may be greater than 24.

No two students can use a laptop at the same time, 
but immediately after a student is done using a laptop, another student can use that same laptop.
For example, if one student rents a laptop during the time interval [0, 2], another student can rent the same laptop during any time interval starting with 2.

Write a function that returns the minimum number of laptops that the school needs to rent such that all students will always have access to a laptop when they need one.

Sample Input: times = [[0, 2], [1, 4], [4, 6], [0, 4], [7, 8], [9, 11], [3, 10]]

Sample Output: 3

Lets use the same algorithm as meeting rooms:
start_times = [0 , 0 , 1, 3, 4, 7, 8]
end_times= [2, 4, 4, 6, 8, 10, 11]
"""

times = [[0, 2], [1, 4], [4, 6], [0, 4], [7, 8], [9, 11], [3, 10]]

def laptopRentals(intervals):
    startTimes = sorted([i[0] for i in intervals])
    endTimes = sorted([i[1] for i in intervals])
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

print((laptopRentals(times)))




