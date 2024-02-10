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



Linda = Person('Wawira')   

print(Linda.age)
print(Linda.name)