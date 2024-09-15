def listsum(x):
    sum = 1
    for i in x:
        sum = sum * i
    return sum


def enter():
    x = []
    for i in range (1, 6):
        l = int (input("Enter Number: "))
        x.append(l)
    return x

print()
x = enter()  
print()
print("List of Numbers: ", x)
print()
print("Product of Numbers: ", listsum(x)) 
print()



