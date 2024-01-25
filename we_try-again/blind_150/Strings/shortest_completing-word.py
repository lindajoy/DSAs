"""
Given a string licensePlate and an array of strings words, find the shortest completing word in words.

A completing word is a word that contains all the letters in licensePlate.
Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. 
If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. 
Possible completing words are "abccdef", "caaacab", and "cbca".

Return the shortest completing word in words. 
It is guaranteed an answer exists. 
If there are multiple shortest completing words, return the first one that occurs in words.


"""
# licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
# Output: "steps"

# Question for interviewer
#   => Shall we always skip the numerical letters or rather are we always assured that the words,are in English and will not contain numbers within the words?
#   => Can we assume that the string of words will always be in lower case?

def shortestCompletingWord(licensePlate, words):
    characters = [i.lower() for i in licensePlate if i.isnumeric() == False and i != '' and i != ' ']
    string_1 = ''.join(sorted(characters))
    print(string_1)
    words2 = []
    res = ''

    for i in range(len(words)):
        modified_str = ''.join(sorted(words[i]))
        if string_1 in modified_str:
            words2.append(words[i])

    print(words2)
    res = words2[0]
    for i in range(1, len(words2)):
        if len(res) > len(words2[i]):
            res = i
       

    return res
        

    
            
        

print(shortestCompletingWord("Ah71752", ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"]))
