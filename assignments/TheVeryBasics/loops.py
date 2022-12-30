"""

Here we will do some dive on for, while , do while refresher using Python

"""

# If statement
# x = int(input("Please enter an integer: "))
x = 9
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

'''
Some notes on the if statement are the else or elif bit is optional.
An if … elif … elif … sequence 
is a substitute for the switch or case statements found in other languages.

Match statements => statement takes an expression and compares its value to successive patterns given as one or more case blocks.
'''
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


'''
Enumerate() Returns an enumerate object. Iterable must be a sequence, 
            an iterator or some object that
supports iteration.
'''

rickMorty = ['Rick', 'Morty', 'Jerry', 'Jane']
print('Enumeration created this:',list(enumerate(rickMorty)))



