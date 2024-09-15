class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14 * radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def __str__(self):
        return (f"Circle With Radius: {self.radius}\n"
                f"Area: {(self.area())}\n"
                f"Circumference: {(self.circumference())}")


radius = float(input("Enter Radius Of the Circle: "))

s1 = Circle (radius)
print(s1)