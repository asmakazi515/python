# Class 
class MyClass:
    x = 5

    def print_x(self):
        print(self.x)

# object
obj = MyClass()

obj.x = 10
obj.print_x() # prints 10

#inheritance
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

  #encapsulation
  class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def _get_age(self):
        return self._age

#polymorphism
class Shape:
  def area(self):
  pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius ** 2)

#abstraction 
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
