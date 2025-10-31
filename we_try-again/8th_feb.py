# This solution does not work well.
def clearDigits(s: str) -> str:
    # What is the input? A string
    # What is the output? A string.
    lst = [str(i) for i in range(10)]
    print(lst)

    left = 0
    splitted_str = [ch for ch in s]

    print(splitted_str)
    
    
    # The sad thing here is i am not sure whether with the current mutations(splitted_str considers)
    # the adjustment in lengths...
    for i in range(len(splitted_str)):
        # print(left)

        if  splitted_str[i] in lst:      
            del splitted_str[i]
            del splitted_str[i - 1]
        print(splitted_str)
    return ''.join(splitted_str)


def clearDigits2(s: str) -> str:
    # Initialize a left pointer at index 0
    left = 0
    # Converts this to a list 
    # s = list(s)
    s = [ch for ch in s]
    lst = [str(i) for i in range(10)]

    for i, c in enumerate(s):
        if c in lst and  left>0:
            left -= 1
            print(left)
        else:
            
            s[left] = c

            left += 1
    s=s[:left]
    return "".join(s)


clearDigits2('cb34')
# Enumerate => returns a list with a number and index

cities = ['Nairobi', 'Kisumu', 'Eldoret', 'Mombasa']

# Generates an index alongside the value.
enum_list = [(i, val) for i, val in enumerate(cities)]
print('Enumerated List', enum_list)