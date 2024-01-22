"""
Given two strings, return true if they are one edit away from each other,else return false.
An edit is insert/replace/delete a character. 
Ex. {"abc","ab"}->true, {"abc","adc"}->true, {"abc","cab"}->false

"""

def oneEdit(string1, string2):
    string1Ptr, string2Ptr = 0, 0
    count = 0

    while string1Ptr < len(string1) and string2Ptr < len(string2):
        if string1[string1Ptr] != string2[string2Ptr]:
            count += 1
            if count > 1:
                return False  # More than one difference found

            # Move the pointer of the longer string
            if len(string1) > len(string2):
                string1Ptr += 1
            elif len(string2) > len(string1):
                string2Ptr += 1
            else:
                # If lengths are equal, move both pointers
                string1Ptr += 1
                string2Ptr += 1
        else:
            string1Ptr += 1
            string2Ptr += 1

    # Check if there is a remaining character in either string
    if string1Ptr < len(string1) or string2Ptr < len(string2):
        count += 1
        
    return True if count == 1 else False

print(oneEdit("abcde", "abcd"))
print(oneEdit("hello", "hello"))
print(oneEdit("rain", "ran"))
print(oneEdit(" ", " "))
print(oneEdit("open", "oppen"))
print(oneEdit("abc", "aefbc"))
print(oneEdit("abc", "cab"))


