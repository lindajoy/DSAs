"""
FIND COMMON CHARACTERS IN WORDS.

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). 
You may return the answer in any order.

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

"""

def find_common_characters(words):
    # This is our result variable.
    res = []

    # Always remember that the sorted always returns a list.
    first_word = sorted(set(words[0]))

    for char in first_word:
        # Here we are generating a list and getting the minimum count within the words.
        frequency = min(word.count(char) for word in words)
        concat = [char] * frequency
        res.extend(concat)

    return res

print(find_common_characters(["bella","label","roller"]))

# Hmm lemme try something here:
random_list = [23, 56, 11, 89, 45, 32, 7, 98, 17, 62]

maximum_value = max(i * 2 for i in random_list)
minimum_value = min(i * 2 for i in random_list)
float_list = [i * 0.002 for i in  random_list ]

print('Float List:', float_list)
print('Max Value:', maximum_value)
print('Min Value:', minimum_value)

