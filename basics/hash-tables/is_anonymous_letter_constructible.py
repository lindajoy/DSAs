"""

Write a program which takes text for an anonymous letter and text for a magazine and determines 
if it is possible to write the anonymous letter using the magazine. 
The anonymous letter can be written using the magazine if for each character in the anonymous letter, 
the number of times it appears in the anonymous letter is no more than the number of times it appears in the magazine.
"""

def is_letter_constructible(anonymous_letter, magazine):
    # Initialize a magazine count
    magazine_hash = {}

    for s in magazine:
        magazine_hash[s] = magazine_hash.get(s, 0) + 1

    for i in range(len(anonymous_letter)):
        if anonymous_letter[i] in magazine_hash and magazine_hash[anonymous_letter[i]] > 0:
            magazine_hash[anonymous_letter[i]] -= 1
        else:
            return False
    return True
   

print(is_letter_constructible('hello', 'hello world'))
print(is_letter_constructible("code", "abcodf"))
print(is_letter_constructible('youareagreathuman', 'eaartygamomneltrrouean'))


# Oooh was to test this

x = "hello"
y = x.replace('l', 'k')
print(y)
   


     