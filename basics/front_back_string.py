# FRONT BACK QUESTION

# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back

# 💡 I really liked this question because it really tests the basics on strings

def front_back(a, b):
    def divide_string(s):
        mid = len(s) // 2
        front = s[:mid + len(s) % 2]
        print('Front',front)
        back = s[mid + len(s) % 2:]
        print('Back',back)
        return front, back
    
    # This actually makes sense
    a_front, a_back = divide_string(a)
    b_front, b_back = divide_string(b)
    return a_front + b_front + a_back + b_back

# Something that I always seem to forget:
random_string = "HelloWorlds"
random_string2= "HelloWorlds"
print(front_back(random_string, random_string2))

# This one includes the fourth index.
print(random_string[4:])
# This does not include the fourth index.
print(random_string[:4])

