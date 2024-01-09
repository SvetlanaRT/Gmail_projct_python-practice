import math

class Shape:
    def __init__(self, color="unknown"):
        self.color = color

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side_length, color="unknown"):
        super().__init__(color)
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

class Circle(Shape):
    def __init__(self, radius, color="unknown"):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Example usage:
square = Square(5)
print(f"Area of the square: {square.area()}, Color: {square.color}")

circle = Circle(3)
print(f"Area of the circle: {circle.area()}, Color: {circle.color}")
