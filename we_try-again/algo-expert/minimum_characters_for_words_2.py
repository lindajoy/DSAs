"""
Write a function that takes in an array of words and returns the smallest array of characters needed to form all of the words.
The characters don't need to be in any particular order.

For example, the characters ["y", "r", "o", "u"] are needed to form the words ["your", "you", "or", "yo"].

Note: the input words won't contain any spaces; however, they might contain punctuation and/or special characters.

Input: words = ["this", "that", "did", "deed", "them!", "a"]
Output:
["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]
// The characters could be ordered differently.
"""

words  = ["this", "that", "did", "deed", "them!", "a"]

# We would like to print out the minimum number of words that are able to form all the words.
def word_count(words):
    # Initialize a dictionary
    char_count = {}
    word_total = []

    for i in words[0]:
        char_count[i] = char_count.get(i, 0) + 1

    for i in words[1:]:
        for word in i:
            if word in char_count:
                char_count[word] = max(char_count[word], i.count(word))
            else:
                char_count[word] =char_count.get(word, 0) + 1

    for k, val in char_count.items():
        count_total = [k]* val
        word_total.extend(count_total)

    return word_total

# The append method adds another element towards the end of the list
# While extends adds another iterable towards the end of the list.

print(word_count(["this", "that", "did", "deed", "them!", "a"]))