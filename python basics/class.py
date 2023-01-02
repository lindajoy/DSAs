"""
(Refresher) Understanding classes in Python 😁
"""

# Create a class named myClass, with a property named x:
class MyClass:
    x = 5

# Now we can use the class named MyClass to create the class named MyClass to create objects

p1 = MyClass()
print('😁',p1.x)

# The __init__() function is used to assign values to the object properties or other operations that are necessary
# to do when the object is being created.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print('Name is:', p1.name)
print("Age is:", p1.age)
print(p1)

# The __str__() function controls what should be returned when the class object is represented as a string.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} {self.age}"


p1 = Person('John', 36)

print(p1)

# The self parameter is a reference to the current instance of the class and is used to access variables that belong to the class
# It does not have to be self you can call it whatever you like, but it has to be the first parameter of any function in the class.


class HelloJoy:
    def __init__(sillObject, someString, year):

        sillObject.someString = someString
        sillObject.year = year 

    def __str__(silObject) -> str:
        return f"{silObject.someString} => {silObject.year}"


sillyObj = HelloJoy('You can do this', 2023)

print(sillyObj)
