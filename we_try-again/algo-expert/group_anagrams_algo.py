"""
Write a function that takes in an array of strings and groups anagrams together.

Anagrams are strings made up of exactly the same letters, where order doesn't matter.
For example, "cinema" and "iceman" are anagrams; similarly, "foo" and "ofo" are anagrams.

Your function should return a list of anagram groups in no particular order.

Input: words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
Output : [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
"""
from collections import defaultdict

def group_anagrams(words):
    words_dict = defaultdict(list)

    for i in words:
        sorted_word = ''.join(sorted(i))
        words_dict[sorted_word].append(i)

    return list(words_dict.values())

print(group_anagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))


   