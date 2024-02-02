"""
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
"""

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]

# You are given an array of words, and you have to output the common characters that are in all of the cahracters
# This is an interesting question.
def common_characters(words):
    if not words:
        return []
    
    res = []
    word1 = set(words[0])

    for letter in word1:
        freq = min([word.count(letter) for word in words])
        res += [letter] * freq
    return res

print(common_characters(["bella","label","roller"]))
print(common_characters(["cool","lock","cook"]))
