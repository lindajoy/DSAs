"""
ﬠ⺢  Reverse All Words in A string.

Given a string containing a set of words separated by whitespace, 
we would like to transform it to a string in which the words appear in the reverse order.
For example, "Alice likes Bob" transforms to "Bob likes Alice". We do not need to keep the original string.
Implement a function for reversing the words in a string s.
"""

# Question for interviewer
#   1. Can we always assume that there will always be a valid input?
#   2. So if i am given a string like:
#           Joy will get into google => google into get will Joy
#           hello world = world hello
#           joy = joy

# Hmm I am thinking of looping the entire string from the end
# And then concatenating to the output string

def reverse_words_in_a_string(str):
    # # Validate the input
    # if not str:
    #     return ""
    
    output_str = ""

    for i in range(len(str) - 1, -1, -1):
        if str[i] == " ":
            # After and before the index.
            # Forgot about the before and after the index
            sliced_str = str[i:]
            str = str[:i]
            output_str += sliced_str

    return output_str + ' ' + str

print(reverse_words_in_a_string("AlgoExpert is the best!"))

# Using the Two pointers
def reverse_words_in_a_string_list(str):
    string_list = str.split(" ")
    print(string_list)
    left, right = 0, len(string_list) - 1

    while left < right:
        string_list[left], string_list[right] = string_list[right], string_list[left]
        left += 1
        right -= 1

    return ' '.join(string_list)



print(reverse_words_in_a_string_list("AlgoExpert is the best!"))
