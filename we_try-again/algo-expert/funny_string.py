"""
In this challenge, you will determine whether a string is funny or not. 
To determine whether a string is funny, create a copy of the string in reverse e.g. abc -> bca
Iterating through each string, compare the absolute difference in the ascii values of the characters at positions 0 and 1, 1 and 2 and so on to the end. 
If the list of absolute differences is the same for both strings, they are funny.

Determine whether a give string is funny. If it is, return Funny, otherwise return Not Funny.

Example:

s = "lmnop"

The ordinal values of the characters are [108,109,110,111,112].
s.reverse = "ponml" and the ordinal values are [112,111,110,109,108].
The absolute differences of the adjacent elements for both strings are [1,1,1,1], so the answer is funny

"""
# What is the input? A string
# What is the output? Can either be Funny or Not Funny

# What went wrong? Did not read through the question well 🥹

def funny_string(s):
    if isinstance(s, int):
        return "Not Funny"
    
    # Ordinal conversion of the string s into list
    ordinal_list = [abs(ord(s)) for s in s][::-1]
    left, right = 0, 1
    difference_list = []
    random_set = set()

    while right < len(ordinal_list):
        diff = ordinal_list[left] - ordinal_list[right]
        difference_list.append(diff)
        left = right
        right += 1
   
    for i in difference_list:
        if i in random_set:
            return "Funny"
        else:
            random_set.add(i)
    return "Not Funny"

print(funny_string("abc"))
print(funny_string("acxz"))
print(funny_string("bcxz"))
print(funny_string("ivvkxq"))
print(funny_string("ivvkx"))
print(funny_string(2))


print(max([2,9,10,5]))

