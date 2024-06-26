"""
GROUP ANAGRAMS

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

def group_anagrams(strings):
    output = {}

    for i in strings:
        sorted_i = ''.join(sorted(i))
        if sorted_i in output:
            output[sorted_i].append(i)
        else:
            output[sorted_i] = [i]

    return list(output.values())
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
