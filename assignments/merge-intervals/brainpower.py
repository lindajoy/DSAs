"""
You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].

The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0)
and make a decision whether to solve or skip each question. Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions.
If you skip question i, you get to make the decision on the next question.

For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
If instead, question 0 is skipped and question 1 is solved, 
you will earn 4 points but you will be unable to solve questions 2 and 3.


Return the maximum points you can earn for the exam.

Input: questions = [[3,2],[4,3],[4,4],[2,5]]
Output: 5

Leetcode question: 
"""

def mostPoints(questions):
    maximumPoints = 0

    if len(questions) == 1:
        return questions[0][0]

    for i in range(len(questions)):
        total_sum = 0
        total_sum += questions[i][0]

        # Move to the next possible step
        next_step = questions[i][1] + (i + 1)
       
        last_index = len(questions) - 1

        if next_step <= last_index:
            total_sum += questions[next_step][0]         

        maximumPoints = max(maximumPoints, total_sum)

    return maximumPoints



x = [[3,2],[4,3],[4,4],[2,5]]
y = [[1,1],[2,2],[3,3],[4,4],[5,5]]
z = [[12,46],[78,19],[63,15],[79,62],[13,10]]

print(mostPoints(z))
print(mostPoints(y))
print(mostPoints(x))

"""
Dynamic Programming => Caching Method
"""

def mostPoints2(questions):
    # We need to have an empty dictionary which acts as our cache
    dfs = {}

    def dfs(i):
        if i >= len(questions):
            return 0

        if i in dfs:
            return dfs[i]

        print(max(dfs(i + 1), dfs(questions[0][0] + questions[i][1] + (i + 1))))
        
        dfs[i] = max(dfs(i + 1), dfs(questions[0][0] + questions[i][1] + (i + 1)))

        return dfs[i]


print(mostPoints2(z))