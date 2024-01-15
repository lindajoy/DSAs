"""
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). 
You may return the answer in any order.
Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
"""

def findCommonCharacters(words):
    res = []
    # Given the input: ["bella","label","roller"]

    # Initialize the first word to be a set
    unique_word_one = set(words[0])
    print(unique_word_one)
    # First word would be bela

    for char in unique_word_one:
        # We get the minimum frequency for a char in each of the words.
        frequency = min(word.count(char) for word in words)
        print('for char {0}, here  was the frequency {1}'.format(char, frequency))
        res += [char] * frequency
    return res

print(findCommonCharacters(["bella","label","roller"]))

# You forgot about the word.count method in strings
my_string = 'Today is a good day'
print('The fr',my_string.count('o'))

# Quick question: If i had a list: Lets start with an empty list

my_empty_list = []
my_list_with_three_ones = [1] * 3
print (my_empty_list + my_list_with_three_ones)

# We can easily concatenate two lists.
first_names = ['Joy', 'Ann', 'Justin']
second_names = ['Lidah', 'Mukami', 'Mwenda']

all_names = first_names + second_names
print("Hello here are all the names:", all_names)