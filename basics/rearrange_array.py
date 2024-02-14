"""
💡 REARRANGE ARRAY

You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:
    Every consecutive pair of integers have opposite signs.
    For all integers with the same sign, the order in which they were present in nums is preserved.
    The rearranged array begins with a positive integer.

Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

What is the input? An array of integers
What is the output? An modified arrangement of the array
"""
# It worked 😄
def rearrange_array(nums):
    positive_integers = [ num for num in nums if num > 0]
    negative_integers = [ num for num in nums if num < 0]
    combined_integers = []
    # We need to append our array such that it will always take one element from the positive integers and another from the negative integers.
    positive_pointer, negative_pointer = 0, 0

    while positive_pointer < len(positive_integers) and negative_pointer < len(negative_integers):
        combined_integers.append(positive_integers[positive_pointer])
        combined_integers.append(negative_integers[negative_pointer])
        positive_pointer += 1
        negative_pointer += 1
    return combined_integers

        

print(rearrange_array([3,1,-2,-5,2,-4]))