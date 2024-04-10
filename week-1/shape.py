class Shape:
     
    # common for all instances 
    desc = " A rectangle is a paralellogram"

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

class Rectangle(Shape):
    def __init__(self, name, x,y):
        super().__init__(name)
        self.x = x
        self.y = y
    
    def area(self):
        return self.x * self.y
    
    def perimeter(self):
        return 2 * (self.x + self.y)
    

rec = Rectangle("Rectangle", 10, 20)

# Intsance variavale
rec.description = "A rectangle comprises of four sides and the length of opossite sides are equal and they are parallel to each other."

print(rec.area())
print(rec.perimeter())
print(rec.description)
print(rec.desc)

