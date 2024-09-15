def list(n):
    if n <= 1:
        return n[0]
    else:
        return n[0] + list(n[1:])
    






print(list[1, 2, [3, 5], [5, 6]])