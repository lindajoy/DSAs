"""
FIND THE LONGEST SUBARRAY WITHOUT REPEATING CHARACTERS.

Write a program that takes an array and returns the length of a longest subarray with the property that all its elements are distinct. 
For example,if thearrayis (f,s,f,e,t,w,e,n,w,e) thenalongest subarray all of whose elements are distinct is (s, f ,e,t,w).
"""

def findLongestSubarrayWithoutRepeatingCharacters(arr):
    # Records the most recent occurences of each entry
    most_recent_occurences = {}

    # Initialize the longest duplicate free subarray as 0
    # Initialize result to 0
    longest_dup_free_subarray, result = 0, 0

    # Loop through the array; We enumerate here we get the index and the element we are looping through in our array.
    # So help me God!
    for i, a in enumerate(arr):
        if a in most_recent_occurences:
            duplicated_index = most_recent_occurences[a]

            if duplicated_index >= longest_dup_free_subarray:
                result = max(result, i - longest_dup_free_subarray )
                longest_dup_free_subarray = duplicated_index + 1

        most_recent_occurences[a] = i

    return max(result, len(arr) - longest_dup_free_subarray)

print(findLongestSubarrayWithoutRepeatingCharacters(['f','s','f','e','t','w','e','n','w','e']))

