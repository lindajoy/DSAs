"""
💡 REVERSE WORDS IN A STRING

Write a function that takes in a string of words separated by one or more whitespaces 
and returns a string that has these words in reverse order. 
For example, given the string "tim is great", your function should return "great is tim".

For this problem, a word can contain special characters, punctuation, and numbers. 
The words in the string will be separated by one or more whitespaces, 
and the reversed string must contain the same whitespaces as the original string. 
For example, given the string "whitespaces 4" you would be expected to return "4 whitespaces".

Note that you're not allowed to to use any built-in split or reverse methods/functions. 
However, you are allowed to use a built-in join method/function.

Also note that the input string isn't guaranteed to always contain words.
"""
"""
Example 1:

sample_input =  "AlgoExpert is the best!"
sample_output = "best! the is AlgoExpert"

Example 2:
sample_input = "Joy will get into google"
sample_output = "google into get will joy"
"""

def reverseWordsInString(sample_str):
    output_str = ''
    
    # Looping in reversal.
    for i in range(len(sample_str)-1, -1, -1):
        if sample_str[i] == " ":
            sliced_str = sample_str[i:]
            sample_str = sample_str[:i]
            output_str += sliced_str 
            continue
    return output_str + ' ' + sample_str

print(reverseWordsInString('AlgoExpert is the best!'))
print(reverseWordsInString("Joy will get into google"))
