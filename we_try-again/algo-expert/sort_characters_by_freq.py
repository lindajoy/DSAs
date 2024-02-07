"""
💡 SORT CHARACTERS BY FREQUENCY

Given a string s, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
"""

# Using a hash map
def sortFrequency(s):
    count = {}
    empty_str = ''

    for i in s:
        count[i] = count.get(i, 0) + 1

    count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    for i, k in count:
        freq = i * k
        empty_str += freq

    return empty_str

print(sortFrequency('tree'))


# Using a List
def frequencySort(s: str) -> str:
    count = []
    str_concat = ""
    # Here we are creating a hashmap.
    # What if we did a list instead?

    for i in set(s):
        freq = s.count(i)
        str_count = [i, freq]
        count.append(str_count)

    # Why does not sort work here well?
    count = sorted(count, key=lambda x: x[1], reverse=True)

    for c, i in count:
        pr = c * i
        str_concat += pr

    return str_concat
        
# 💡 Using Default Dictionary Instead
from collections import Counter, defaultdict
def frequencySort2(s: str):
    count_chars = Counter(s) # char -> cnt
    buckets = defaultdict(list)
    # Hmm, I would not have done it this way

    for char, cnt in count_chars.items():
        buckets[cnt].append(char)

    print("Buckets:", buckets)
    res = []

    for i in range(len(s), 0, -1):
        for c in buckets[i]:
            res.append(c*i)
    return "".join(res)

print(frequencySort2('tree'))

