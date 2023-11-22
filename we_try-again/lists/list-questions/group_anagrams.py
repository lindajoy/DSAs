# This question led me to understand a little bit more about/ operations done in Python dictionaries.
# Check Randoms/dictionaries.py

"""
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1: 
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: sts = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""
from collections import defaultdict


strs = ["eat","tea","tan","ate","nat","bat"]

def groupAngrams(lst):
    # Create a map.
    # Here we are initializing a dictionary with an empty list.
    anagram_dict = defaultdict(list)

    # Loop through the list;  Find the sorted key, and append the anagram; This is a cleaner way of doing things 🤔!
    for i in lst:
        sorted_word = "".join(sorted(i))
        anagram_dict[sorted_word].append(i)
    return list(anagram_dict.values())

print(groupAngrams(strs))