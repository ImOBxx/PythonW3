def row():
    l = [1, 2, 3, 3, 3, 3, 4, 5]
    s = []
    for i in l:
        if i not in s:
            s.append(i)
    return s

print(row())