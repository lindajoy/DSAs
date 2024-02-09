"""
Write a function that takes in an array of words and returns the smallest array of characters needed to form all of the words.
The characters don't need to be in any particular order.

For example, the characters ["y", "r", "o", "u"] are needed to form the words ["your", "you", "or", "yo"].

Note: the input words won't contain any spaces; however, they might contain punctuation and/or special characters.
"""

# INPUT: words = ["this", "that", "did", "deed", "them!", "a"]

# OUTPUT: ["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]
# The characters could be ordered differently.

# ❌ COPIED THE FIRST SOLUTION FROM CHATGPT DID NOT WORK.
def minimumCharactersForWords(words):
    if not words:
        return []
    
    # Create a dictionary to store the frequency of each character in word
    char_frequency = {}

    # Iterate through each word and update the characters frequency
    for word in words:
        for char in word:
            char_frequency[char] = char_frequency.get(char, 0) +1

    print('CHARACTER FREQUENCY:', char_frequency)
    # Create the smallest set of characters needed
    smallest_set = []
    for char_word, freq in char_frequency.items():
        smallest_set.extend([char_word] * min(freq, words.count(char)))
    return smallest_set
print(minimumCharactersForWords(["this", "that", "did", "deed", "them!", "a"]))

lst = ["this", "that", "did", "deed", "them!", "a"]
lst.count('😄','a')
# 💡 SECOND SOLUTION USING DEFAULTDICT
from collections import defaultdict

# O(n) time  | O(n) space where n is length of the word
def get_word_characters(word):
    char_count = {}
    for char in word:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

# O(n * time)  | O(c) space
# where n is the number of words, 1 length of the longest word, c is the number of unique characters.
def minimumCharactersForWords2(words):
    min_character_count = defaultdict(int)
    print(min_character_count)
    
    for word in words:
        word_char_count = get_word_characters(word)
        for char in word_char_count:
            # Update count if we find a word that needs more
            min_character_count[char] = max(
                min_character_count[char], word_char_count[char]
            )

    # Convert hash table to list
    min_character_list = []
    for char in min_character_count:
        count = min_character_count[char]
        min_character_list.extend([char] * count)
    
    return min_character_list

print(minimumCharactersForWords2(["this", "that", "did", "deed", "them!", "a"]))

# 💡 Refresher on Default Dictionary
random_dict = defaultdict(int)
print("Here is my default dictionary:", random_dict)

# 💡 Random fun fact
random_dict2 = {'hello': 'world', 'foo': 'bar'}

# These two do the same thing! 🤔
for i in random_dict2:
    print(i)

for i in random_dict2.keys():
    print(i)