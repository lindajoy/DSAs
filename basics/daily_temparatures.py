"""
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# 💡 Example 2
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]

# 💡 Example 3
# Input: temperatures = [30,60,90]
# Output: [1,1,0]

def dailyTemparatures(temparatures):
    results = [0] * len(temparatures)
    stack = []

    # This makes better sesnse
    for i, t in enumerate(temparatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            print('Index:',stackInd)
            results[stackInd] = (i - stackInd)
        stack.append([t,i])
    return results
    

print(dailyTemparatures([73,74,75,71,69,72,76,73]))
