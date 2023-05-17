def validPalindrome( s):
    l, r = 0, len(s) - 1

    while l < r:
        if s[l] != s[r]:
            skipL, skipR = s[l + 1: r + 1], s[l:r]

            print("Skip Left", skipL, "Skip Right", skipR)
            print("Reversed Skip Left", skipL[::-1], "Reversed Skip Right", skipR[::-1])


            return (skipL == skipL[::-1] or skipR == skipR[::-1])

        l, r = l + 1, r - 1

    return True

print(validPalindrome('abc'))
