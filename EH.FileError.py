print()
try:
    f = open('test1.txt')
except:
    print("Wrong File")
else:
    print(f)
finally:
    print("The Code Is Executed.")
print()