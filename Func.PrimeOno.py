def prime(n):
    count = 0
    for i in range (1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print("The Number Is A Prime Number. ")
    else:
        print("The Number Is Not A Prime Number. ")

n = int (input ("Enter Number: "))
(prime(n))


