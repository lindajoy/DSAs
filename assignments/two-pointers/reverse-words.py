"""
EDUCATIVE REVERSE WORDS

Given a sentence, reverse the order of its words without affecting the order of letters within a given word.

Example: Welcome to Educative!
         Should be Educative! to Welcome


Two pointers 

"""

# 💡 Naive Approach => Wrong solution

my_string = 'Welcome to Educative'
string_two = 'Hello World'
my_string2 = my_string[::-1]
# print('Here is my reversed string',my_string2)
# print(string_two.split())


# Solution using two pointers
# 1. We can create a list from the sentence
# 2. Loop the entire array, swap the left pointer value with the right pointer value.
# 3. Achieving the optimum reversal

def reverse_words(string):
    string_list = string.split()
    left = 0
    right = len(string_list) - 1

    while left < right:
        string_list[left], string_list[right] = string_list[right], string_list[left]
        left += 1
        right -= 1

    return " ".join(string_list)


print('Example One', reverse_words('Hello World'))





