"""
Write a function that takes in an array of words and returns the smallest array of characters needed to form all of the words.
The characters don't need to be in any particular order.

For example, the characters ["y", "r", "o", "u"] are needed to form the words ["your", "you", "or", "yo"].

Note: the input words won't contain any spaces; however, they might contain punctuation and/or special characters.
"""

# INPUT: words = ["this", "that", "did", "deed", "them!", "a"]

# OUTPUT: ["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]
# The characters could be ordered differently.

def minimumCharactersForWords(words):
    starting_word = words[0]
    start_dictionary = {}

    for i in starting_word:
        if i in starting_word:
            start_dictionary[i] = 1
        else:
            start_dictionary[i] += 1
    for i in range(1, len(words)):
        word_in = words[i]

        for i  in word_in:
            if i in word_in:
                freq = max(start_dictionary[i], )
                start_dictionary[i] 
            

print(minimumCharactersForWords(["this", "that", "did", "deed", "them!", "a"]))

