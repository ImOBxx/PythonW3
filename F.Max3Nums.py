
def Enter():
    a = int (input ("Enter A: "))
    b = int (input ("Enter B: "))
    c = int (input ('Enter C: '))
    if a > b and a > c:
        print("A Is The Greatest.")
    elif b > a and b > c:
        print("B Is The Greatest.")
    else:
        print("C Is The Greatest")
    return a, b, c





print((Enter()))
    
