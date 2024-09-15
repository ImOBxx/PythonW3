l = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original List: ", l)

l.sort(key = lambda x : x[1])

print("Sorted List: ", l)

