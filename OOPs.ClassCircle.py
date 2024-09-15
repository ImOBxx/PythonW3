class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14 * self.radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def __str__(self):
        return (f"Circle with radius: {self.radius}\n"
                f"Area: {(round(self.area()))}\n"
                f"Circumference: {(round(self.circumference()))}")

radius = float(input("Enter Radius Of The Circle: "))

s1 = Circle(radius)
print(s1)


