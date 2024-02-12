"""
💡 Valid IP Addresses

You're given a string of length 12 or smaller, containing only digits. 
Write a function that returns all the possible IP addresses that can be created by inserting three .s in the string.

An IP address is a sequence of four positive integers that are separated by .s, 
where each individual integer is within the range 0 - 255, inclusive.

An IP address isn't valid if any of the individual integers contains leading 0s.
For example, "192.168.0.1" is a valid IP address, but "192.168.00.1" and "192.168.0.01" aren't, because they contain "00" and 01, respectively. 
Another example of a valid IP address is "99.1.1.10"; conversely, "991.1.1.0" isn't valid, because "991" is greater than 255.

Your function should return the IP addresses in string format and in no particular order. 
If no valid IP addresses can be created from the string, your function should return an empty list.
"""

# Hmm did not understand this question. 🤔

# What is the input? A string
# What is the output? Number of Valid IP Adresses that can be formed from the string.
# We need to insert like 3 dots form an IP Adresss

# THREE CONDITIONS SATISFY A VALID IP ADRESS:
#       =>  Each individual integer should not be greater than 255
#       =>  No, leading 0s.

def get_valid_ip_address(s):
    # Helper function
    def is_valid_part(s):
        return len(s) == 1 or (s[0] != 0 and int(s) <= 255)
    
    result, parts = [], [None] * 4
    
    for i in range(1, min(4, len(s))):
        parts[0] = s[:i]

        if is_valid_part(parts[0]):
            for j in range(1, min(len(s) - i, 4)):
                parts[1] = s[i:i + j]
                if is_valid_part(parts[1]):
                  for k in range(1, min(len(s) - i - j, 4)):
                      parts[2],parts[3]=s[i +j:i +j +k], s[i +j +k:]
                      if is_valid_part(parts[2]) and is_valid_part(parts[3]):
                          result.append(''.join(parts))


    return set(result)

print(get_valid_ip_address("1921680"))

for i in range(1, min(4, len('1921680'))):
    print('😁',i)
