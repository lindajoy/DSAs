def reverseString(string):

    strList = string.split()
    # Reversing a string
    strList = strList[::-1]
    
    return ' '.join(strList)

if __name__ == '__main__':
    print(reverseString("Alice Likes Bob"))


