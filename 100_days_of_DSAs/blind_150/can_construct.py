"""
Given two strings, ransom_note and magazine, check if ransom_note can be constructed using the letters from magazine. 
Return TRUE if it can be constructed, FALSE otherwise.

Example 1: 
Ransom note = "program"
Magazine = "rpgoarm"

Output: True

Example 2:
Ransom note = "code"
Magazine = "abcodf"

Output: False

Question You should ask at this point: 
1. Can you assume that all the letters here are lower case? or are there upper case letters in the strings provided?
2. Should we assume that all characters magazine should be used in my ransom note?
"""

def can_construct(ransom_note, magazine):
    # Create a hash map storing the frequency of all the characters in the string
    magazine_hash = {}
    for s in magazine:
        if s in magazine_hash:
            magazine_hash[s] += 1
        else:
            magazine_hash[s] = 1

    for i in range(len(ransom_note)):
        if ransom_note[i] in magazine_hash and magazine_hash[ransom_note[i]] > 0:
            magazine_hash[ransom_note[i]] -= 1
        else:
            return False
        
    return True
  
print(can_construct('code', 'abcodf'))
print(can_construct('program','program'))
print(can_construct('youareagreathuman', 'eaartygamomneltrrouean'))
print(can_construct('codinginterviewquestions', 'aboincsdefoetingvqtniewonoregessnutins'))
print(can_construct('problemsolving', 'adsoptendroblemfemopvinxtbm'))
print(can_construct('youhaveakindheart', 'abecdefghiavjklmaonopqhrtuvweaxyz'))
# print(can_construct())