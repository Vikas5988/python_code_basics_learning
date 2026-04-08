# Parent class
class Shape:
    def area(self):
        return 0  # Default area is 0

# Child class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width    # Store width
        self.height = height  # Store height

    # Override area() from Shape
    def area(self):
        return self.width * self.height  # width × height

# Child class inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # Store radius

    # Override area() from Shape
    def area(self):
        return 3.14159 * self.radius ** 2  # π × r²

# Create objects
shapes = [Rectangle(5, 3), Circle(4)]

# Loop and call overridden area() on each shape
for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area()}")