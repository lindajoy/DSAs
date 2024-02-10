"""
A class is a blueprint of an object.
"""

# A class is made up of attributes(data) and methods(functions).

class Person(object):
    """A simple class"""
    age = 40

    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return self.name
    
    def rename(self, renamed):
        self.name = renamed
        print("Now my name is {0}".format(self.name))

    def product(self, age):
        return int(age) * 2



Linda = Person('Wawira')   

print(Linda.age)
print(Linda.name)
print(Linda.product(400))


print('{0} {1} {2}'.format('Joy', 'Lidah', 'Wawira'))

# Simplest way of testing whether a string is a palindrome.
my_sample_string = "ababa"
print('In the case of `ababa` should return a positive outcome:', my_sample_string == my_sample_string[::-1])

# Here is a way of reversing a string: my_sample_string[::-1]
# What about if i wanted to use the reversed instead?
my_name = "Joy L Wawira"
reverse = ''.join(reversed(my_name))
print(reverse)
random_list = [40, 50, 60, 70]
print(random_list.reverse())

# Hmm: In conclusion, always use this [::-1] to reverse a list or string
