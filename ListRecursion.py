def list(n):
    if len(n) == 1:
        return n[0]
    else:
        return n[0] + list(n[1:])

print(list([2]))
