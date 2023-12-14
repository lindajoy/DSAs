"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] 
indicates that you must take course b(i) first if you want to take course a(i).
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""

# 💡 Example 1 
# Input: prerequistes => [[1,0],[0,1]]
# Output : False
# Reason: We detect a loop, Hence we cannot finish all courses!


# 💡 Example 2
# Input: prerequistes => [[1,0]]
# Output: True
# Reason: You have to finish course 0 to finish course 1; No loop detected 👻

# What is the input?: A 2grid array of prequisites.
# What is the output:  A boolean(True or False); Depends on whether all courses can be completed!

def canFinish(numCourses, preRequistes):
    preMap = {i: [] for i in range(numCourses)}
    print(preMap)
    for crs, pre in preRequistes:
        preMap[crs].append(pre)
    print("After appending Prerequisites:", preMap)

    # Initialized an empty set
    visit = set()
    stack = []
    def dfs(crs):
        # If crs already in the Visit set it means we have detected a cycle => Hence we cannot complete all the courses.
        if crs in visit:
            return False
        
        # If course has no preRequisites it means it can be completed 👻
        if preMap[crs] == []:
            return True
        
        # Add course on the visit set
        visit.add(crs)

        for pre in preMap[crs]:
            if not dfs(pre):
                return False
        visit.remove(crs)
        stack.append(crs)
        print("Hello Stack:", stack)
        preMap[crs] = []
        return True
        
        #  Loop through the courses, Why we are doing this is because what if the graph is not connected?
    for crs in range(numCourses):
        if not dfs(crs):
            return False
    return True
        
pre = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4]]
pre3 = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [1, 6], [6, 5]]
total_courses = 7
pre2 = [[1, 0], [2, 1], [3, 2]]
num_courses_2 = 4
num_courses = 6
numCourses4 = 4
prerequisites4 = [[1,0],[2,0],[3,1],[3,2]]
# print(canFinish(total_courses, pre3))
print('Boom 2: ',canFinish(numCourses4, prerequisites4))