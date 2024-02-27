"""
It's photo day at the local school, and you're the photographer assigned to take class photos. 
The class that you'll be photographing has an even number of students, and all these students are wearing red or blue shirts.
In fact, exactly half of the class is wearing red shirts, and the other half is wearing blue shirts. 
You're responsible for arranging the students in two rows before taking the photo. 
Each row should contain the same number of the students and should adhere to the following guidelines:
    All students wearing red shirts must be in the same row.
    All students wearing blue shirts must be in the same row.
    Each student in the back row must be strictly taller than the student directly in front of them in the front row.
You're given two input arrays: one containing the heights of all the students with red shirts and another one 
containing the heights of all the students with blue shirts. 

These arrays will always have the same length, and each height will be a positive integer.
 Write a function that returns whether or not a class photo that follows the stated guidelines can be taken.

Note: you can assume that each class has at least 2 students.


"""
redShirtHeights = [5, 8, 1, 3, 4]
blueShirtHeights = [6, 9, 2, 4, 5]

# Each student in the back row should strictly be taller than the student in the front row.

# Should return True
# What if we sort them both first? 
# blue = [2,4,5,6,9]
# red = [1,3,4,5,8]

# redShirtHeights = [4, 7, 3, 6]
# blueShirtHeights = [5, 8, 2, 9]
# When we sort them what do we get?
red = [3, 4, 6, 7]
blue = [2, 5, 8, 9]

# This one assumes that the red people will always be shorter than the blue people.

def classPhotos(reds, blues):
    if not blues or not reds:
        return False
    isBlueGreater = False
    # Here we are sorting the two arrays
    reds.sort()
    blues.sort()

    if reds[0] < blues[0]:
        isBlueGreater = True

    for i in range(len(blues)):
        if (isBlueGreater):
            if reds[i] > blues[i]:
                return False
        elif reds[i] < blues[i]:
            return False
    return True

    
print(classPhotos(redShirtHeights, blueShirtHeights))
