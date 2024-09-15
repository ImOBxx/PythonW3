print()
try:
    print()
    l = [10, 20, 30, 40]
    r = l.length()
    print(r)
except AttributeError:
    print()
    print("Attribue Error")
else:
    print()
    print(len(l))
finally:
    print()
    print("The Code Is Executed.")
print()