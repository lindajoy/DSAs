"""
Custom Sort String

You are given two strings order and s.
All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. 
More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.
"""

# What did you learn from this question?

    # => Reminded me on how to remove elements from a dictionary
    # Say You had a dictionary cities:
    # cities = {'Nairobi': 1000, "Lusaka": 2100, "Eld": 400}
    # If you wish to remove "Eld" is a simple as: cities.pop("Eld")

    # Another thing:
    # if you have a string like: "hello" and would like to convert it to a list: ["h", "e", "l", "l", "o"]


# renaming_reminding_myself_of_rebase

from collections import Counter

def customSortString(order, s):
    res = ''

    s_count = Counter(s)
    for i in range(len(order)):
        if order[i] in s_count:
            count = s_count[order[i]]
            res += order[i] * count
            s_count.pop(order[i])

    if len(res) == len(s):
        return res
    else:
        for key, item in s_count.items():
            res += key * item
        return res

order = "bcafg"
s = "abcd" 

print(customSortString('cba', 'abcd'))
print(customSortString("kqep","pekeq"))
print(customSortString("kqepe","pekeq"))
print(customSortString("monday","daymonnnnn"))


print(customSortString(order, s))
