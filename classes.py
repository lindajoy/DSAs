class Dog:
    species = "Homo Sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    #instance  method
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


miles = Dog("Miles", 4)
print(miles.description())
print(miles.speak('Hello Joy'))

"""
Create a Car class with two instance attributes:

.color, which stores the name of the car’s color as a string
.mileage, which stores the number of miles on the car as an integer
Then instantiate two Car objects—a blue car with 20,000 miles 
and a red car with 30,000 miles—and print out their colors and mileage. Your output should look like this:

The blue car has 20,000 miles.
The red car has 30,000 miles.
"""

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def carsMileage(self):
        return f"The {self.color} has {self.mileage} miles"

blueCar = Car('blue',20000)
print(blueCar.carsMileage())

redCar = Car('red',10000)
print(redCar.carsMileage())


"""

"""

class Solution:
    def fizzBuzz(self, n: int):
        if n%5 == 0 and n%3 == 0:
            return 'Fizzbuzz'
        elif n%3 == 0:
            return 'Fizz'
        elif n%5 == 0:
            return'Buzz'
        else:
            return str(n)
  

final_strings =[Solution(1) for i in range(3)]
print(final_strings)

