"""
How can a given string comprised of lowercase letters be split into the fewest possible substrings,
ensuring that each substring contains only unique letters? 
Return the minimum number of splits needed. For example, "world" should return 5, and "abacdec" should return 3.
"""

# Whats the input? A string
# Whats the output? Number of unique substrings without non repeating characters

# Example: "abacdec"
# Output: 'a', 'bacd', 'ec' or 'ab', 'acde", "c"

# What is the solution?


def numberOfSubstrings(S):
    # We invalidate inputs
    if not S:
        return 0


    if len(set(S)) == len(S):
        return 1
    
    empty_string = ""
    count = 0

    for i in range(len(S)):
        if S[i] in empty_string:
            count += 1
            empty_string = S[i]
        else:
            empty_string += S[i]

    

    return count + 1

print(numberOfSubstrings("abacdec"))
print(numberOfSubstrings("hello"))
print(numberOfSubstrings("abbac"))
print(numberOfSubstrings("abcabc"))