def sentence():
    a_count = 0
    b_count = 0
    s = "The Quick Brown Foxx "
    for c in s:
        if c.isupper():
            a_count += 1
        elif c.islower():
            b_count += 1
    return a_count, b_count

a_count, b_count = sentence()
print("Total UpperCase Characters: ", a_count)
print("Total LowerCase Characters: ", b_count)
