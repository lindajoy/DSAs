"""
💡 Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Sample Input:  strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

"""

from collections import defaultdict

def groupAnagrams(strs):
    # How to defaulDicts work?
    strings = defaultdict(list)

    for i in strs:
        sorted_str = ''.join(sorted(i))
        strings[sorted_str].append(i)

    return list(strings.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))