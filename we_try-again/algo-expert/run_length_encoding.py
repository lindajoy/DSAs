"""
Write a function that takes in a non-empty string and returns its run-length encoding.

From Wikipedia, "run-length encoding is a form of lossless data compression in which runs of data are stored as a single data value and count, rather than as the original run." 
For this problem, a run of data is any sequence of consecutive, identical characters. So the run "AAA" would be run-length-encoded as "3A".

To make things more complicated, however, the input string can contain all sorts of special characters, including numbers. 
And since encoded data must be decodable, this means that we can't naively run-length-encode long runs. 
For example, the run "AAAAAAAAAAAA" (12 As), can't naively be encoded as "12A", since this string can be decoded as either "AAAAAAAAAAAA" or "1AA". 
Thus, long runs (runs of 10 or more characters) should be encoded in a split fashion; the aforementioned run should be encoded as "9A3A".
"""

def runLengthEncoding(string):
    # Initialize an empty list
    result = []
    # The current character is at index 0
    currentChar = string[0]
    # Frequency set to 0
    frequency = 0

    # Loop through each character in the string
    for x in string:
        if x == currentChar:
            if frequency < 9:
                frequency += 1
            else:
                result.append(str(frequency) + currentChar)
                frequency = 1
        else:
            result.append(str(frequency) + currentChar) 
            currentChar = x
            frequency = 1
    result.append(str(frequency) + currentChar)
    return "".join(result)

print(runLengthEncoding("AAAAAAAAAAAA"))
print(runLengthEncoding("AAAABBBCCDAA"))