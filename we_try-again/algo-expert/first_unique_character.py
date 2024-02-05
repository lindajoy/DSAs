"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1

"""

def firstUniqChar(self, s: str) -> int:
        # We can use a hashmap to store the different counts of characters.
        # Then later we filter out the counts of characters with a count of 1
        # With this information we can use the index() function on strings to get
        # the minimum index of a character thus returning the first occurence
        char_count = {}

        for i in s:
            char_count[i] = char_count.get(i, 0) + 1

        lst = [(key) for key,value in char_count.items() if value == 1]
        store_occurences_with_one = sorted([s.index(i) for i in lst])


        if store_occurences_with_one:
          return store_occurences_with_one[0]
        else:
          return -1




       



        