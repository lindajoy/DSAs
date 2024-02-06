"""
💡 COURSE SCHEDULE

Came Here after bumping into the question: Cycle in Graph.
Pretty Interesting way of starting the morning 💃🏾 🌅

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""

# 💡 Key Take Aways:

#  => This question basically asks us to find a cycle within a directed graph, if a cycle is found, then it means all prerequisites cannot be completed.
#  => Building an adjacency list is one of the things that come in handy.

# For this question:
# What is the input? numCourses and a list of prerequisites
# What is the output? A boolean; Indicating whether all courses can be completed or not

def course_schedule_one(numCourses, prerequisites):
    # Dictionary comprehension
    preMap = { i:[] for i in range(numCourses) }

    # Here we are creating an adjacency list with correct mappings.
    for crs, pre in prerequisites:
        preMap[crs].append(pre)

    # Initialize the visit set, this basically helps us find cycle in our visit set if there are.
    visit = set()

    def dfs(course):
        # Base Cases
        if course in visit:
            return False
        if preMap[course] == []:
            return True
        visit.add(course)
        
        for pre in preMap[course]:
            if not dfs(pre): 
                return False
            
        visit.remove(course)
        preMap[course] = []
        return True
    
    for crs1 in range(numCourses):
        if not dfs(crs1):
            return False
    return True

print(course_schedule_one(2, [[1,0], [0,1]]))

