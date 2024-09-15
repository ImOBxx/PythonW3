def power(a, b):
    if b == 1:
        return a
    elif a == 0:
       return 0
    elif b == 1:
       return a
    else:
       return a * power(a, b - 1)

print(f"Product of base {a} to power of {b} is: {power(a, b)}")
print(power(3, 4))
power(a, b)