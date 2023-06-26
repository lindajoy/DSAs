"""
Employee free time

You’re given a list containing the schedules of multiple employees.
Each person’s schedule is a list of non-overlapping intervals in sorted order. 
An interval is specified with the start and end time, both being positive integers.

Your task is to find the list of intervals representing the free time for all the employees.

Sample Input:
[[[3, 5], [8, 10]], [[4, 6], [9, 12]], [[5, 6], [8, 10]]]


Sample Output:
[[6,8]]
"""

"""
Pseudocode:
1. Merge all the lists for each employee append it on one list
"""
Input = [[[3, 5], [8, 10]], [[4, 6], [9, 12]], [[5, 6], [8, 10]]]
Input2 = [[[1, 3], [5, 6], [9, 10]],[[2, 4], [7, 8]], [[8, 11], [12, 14]]]

def findEmployeesFreeTime(schedules):
    merged = []
    free_time = []
    def mergeSingleEmployeesTime(personal_time):
        current_start = personal_time[0][0]
        curent_end = personal_time[0][1]

        for interval in personal_time[1:]:
            if interval[0] < current_start:
                current_start = max(current_start, interval[0])
                curent_end = min(curent_end, interval[1])
                merged.append([current_start, curent_end])
            if interval[0] > curent_end:
                current_start = min(interval[0], curent_end)
                curent_end = max(interval[0],curent_end )
                merged.append([current_start, curent_end])

        return merged.sort(key=lambda x:x[0])

    for i in schedules:
        x = mergeSingleEmployeesTime(i)


   
    print(merged)
    current_start = merged[0][0]
    current_end = merged[0][1]
 
    for i in merged[1:]:
        if i[0] < current_end:
            current_start = max(current_start, i[0])
            current_end = min(current_end, i[1])
            free_time.append([current_start, current_end])

        if i[0] > current_end:
            current_start = min(i[0], current_end)
            current_end = max(i[0],current_end )
            free_time.append([current_start, current_end])


    return free_time

print(findEmployeesFreeTime(Input))
print(findEmployeesFreeTime(Input2))



    
