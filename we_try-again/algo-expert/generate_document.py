"""
You're given a string of available characters and a string representing a document that you need to generate. 
Write a function that determines if you can generate the document using the available characters. 
If you can generate the document, your function should return true; otherwise, it should return false.

You're only able to generate the document if the frequency of unique characters in the characters string is greater than or equal to the frequency of unique characters in the document string.
For example, if you're given characters = "abcabc" and document = "aabbccc" you cannot generate the document because you're missing one c.

The document that you need to create may contain any characters, including special characters, capital letters, numbers, and spaces.

Note: you can always generate the empty string ("").

characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"

"""
# 💡 INPUT
# characters = "Bste!hetsi ogEAxpelrt x "
# document = "AlgoExpert is the Best!"

# OUTPUT =>  true

# QUESTIONS FOR THE INTERVIEWER:
#
# 1. The characters string can be greater or equal to the length of the len(document)?
# 2. Tehcnical question: When we look for the length of the string, does it also calculate the white space?
# 3. 

from collections import Counter

def generateDocument(characters, document):
    # Validating the input first => Does the input exist?
    if not characters or not document:
        return False
    
    # Validate whether the length of characters is equal or greater that lenght of document
    if len(characters) < len(document):
        return False
    
    # We need to create a hashmap containing the count occurences of each alphabet
    chars_map = Counter(characters)

    for i in document:
        if i in document:
            chars_map[i] -= 1
        else:
            return False
        
    return all(value >= 0 for value in chars_map.values())

characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"

print(generateDocument(characters, document))
print(generateDocument("!@#$%^&* 123","!@#$ 2"))
print(generateDocument("abcdxyz","abccdd"))



