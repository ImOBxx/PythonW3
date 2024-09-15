def largest():
    if (a > b and a > c):
        return "1st Number Is The Largest"
    elif (b > a and b > c):
        return "2nd Number Is The Largest"
    elif (c > a and c > b):
        return "3rd Number Is The Largest"

print()
a = int (input("Enter 1st Number: "))
b = int (input("Enter 2nd Number: "))
c = int (input("Enter 3rd Number: "))
print()

print(largest())
print()





