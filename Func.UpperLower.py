def upper(n):
    u_count = 0
    l_count = 0
    for char in n:
       if char.isupper():
        u_count += 1
       elif char.islower():
        l_count += 1
    return l_count, u_count

n = (input ("Enter String: "))
u_count, l_count = upper(n)
print(f"Uppercase count: {u_count}")
print(f"Lowercase count: {l_count}")