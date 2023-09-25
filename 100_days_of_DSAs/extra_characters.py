"""
You are given a 0-indexed string s and a dictionary of words dictionary. 
You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. 
There may be some extra characters in s which are not present in any of the substrings.
Return the minimum number of extra characters left over if you break up s optimally.

Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
"""
"""
Breaking down the question:
"""
s = "leetscode"
sample_string = "leetscode"
print(sample_string in s)

dictionary = ["leet","code","leetcode"]
empty_dict = {}

for i in dictionary:
    empty_dict[i] = len(i)

print('Unsorted Empty Dictionary', empty_dict)
sorted_letters = dict(sorted(empty_dict.items(), key=lambda x: x[1], reverse=True))
print(sorted_letters)

## Dynamic Programming Solution => Not understood this....🥲
s = "leetscode"
dict3 = ["leet","code","leetcode"]

def minimumExtraCharacter(str, dictionary):
    # Remove all the duplicates in my array
    words = set(dictionary)
    # Set up a hash set for caching/memoization
    dp = {}

    # Recursive Function => Always identify the Base Case
    def dfs(i):
        # Means we are the end of the string
        if i == len(str):
            return 0
        if i in dp:
            return dp[i]
        res = 1 + dfs(i + 1) # skip current char
        print(res)

        for j in range(i, len(str)):
            if s[i:j+1] in words:
                print('Here is my string:',s[i:j+1])
                res = min(res, dfs(j + 1))

        dp[i] = res
        return res
    
    return dfs(0)

print(minimumExtraCharacter(s, dict3))