# REPLACE FUNCTION.

# String replace string takes in three parameters:

#   Old substring to search for (Required)
#   New substring to replace with (Required)
#   Count number of occurrences in the string

#   SYNTAX : str.replace(old, new, count)

#   Learnt this from this question: https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/?envType=daily-question&envId=2024-10-07

#   Easiest solution would be:

def minLength(s):
    while "AB" in s or "CD" in s:
        # Replacing strategy through chaining.
        s = s.replace('AB', '', 1).replace('CD', '', 1)
    return len(s)

print(minLength('CCCCDDDD'))

# My solution however at first was through the two pointers solution:

# Did not work though...🥲

def minLength(s):
    left_ptr, right_ptr = 0, 1
    distinct_strs = set(['AB', 'CD'])

    # Get rid of the easiest case
    if len(s) == 0 or s == '':
        return 0

    while right_ptr <= len(s):
        sliced_str = s[left_ptr: right_ptr + 1]
        if sliced_str in distinct_strs:
            s = s[left_ptr: right_ptr + 1]
            if left_ptr > 0:
                left_ptr -= 1
            else:
                left_ptr += 1
        else:
            left_ptr += 1
            right_ptr += 1


    return len(s)
        

        
    