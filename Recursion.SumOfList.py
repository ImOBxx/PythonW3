def compute(n):
    if n <= 0:
        return 0
    else:
        return n + compute(n-1)

total_sum = 0

for i in range(1, 6):
    l = int(input("Enter Number: "))
    print(list(i))
    total_sum += l


print("Total Sum:", total_sum)
