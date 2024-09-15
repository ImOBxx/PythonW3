class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * radius * radius
    
    def circumference(self):
        return 2 * 3.14 * radius
    
    def __str__(self):
        print()
        print("Circle's Computations: ")
        print()
        return (f"Radius Of The Circle: {self.radius}\n"
                f"Area Of The Circle: {self.area()}\n"
                f"Circumference Of The Circle: {self.circumference()}\n")

print()
radius = int (input ("Enter The Radius Of The Circle: "))
print()

s1 = Circle(radius)
print(s1)


