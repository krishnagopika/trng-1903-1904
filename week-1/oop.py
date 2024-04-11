from abc import ABC, abstractmethod

# Multi level inheritance

class Parent:

    def __init__(self, name):
        self.name = name

class Child(Parent):

    def __init__(self, name, role):
        super().__init__(name)
        self.role = role


class GrandChild(Child):

    def __init__(self, name, role, description):
        super().__init__(name, role)
        self.description = description


gc = GrandChild("Sam", "Developer", "Software Engineer")

print(gc.name, gc.role, gc.description)



# Multiple Inheritance
class Vampire:

    def __init__(self) -> None:
        pass

    def description(self):
        return "Cold Blooded"

class Wearwolf:

    def __init__(self) -> None:
        pass

    def hunt(self):
        return "We hunt vampires"

class VampireWearwolf(Vampire, Wearwolf):

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name


klaus = VampireWearwolf("Klaus")

print(klaus.description(), klaus.hunt())


# Abstraction

class Shape(ABC):

    def print_info(self):
        print("I am an Abstact class")

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):

    def __init__(self, x,y):
        self.name = "Rectangle"
        self.x = x
        self.y = y
    # def area(self):
    #     return self.x * self.y
    # def perimeter(self):
    #     return 2*(self.x + self.y)
    

class Square(Rectangle):
  
    def __init__(self,x):
        self.name = "Square"
        self.x = x
        
    
    def area(self):
        return self.x * self.x
    def perimeter(self):
        return 4*self.x

class Circle:

    def __init__(self, radius):

        self.name = "Circle"
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius**2)
    
    def perimeter(self):
        return 2 * 3.14 * self.radius



s = Square(3)
circle = Circle(4)


for i in (s,circle):
    print(i.name)
    # print(i.area())
    print(i.perimeter())
