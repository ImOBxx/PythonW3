class Person:
    def __init__(self, age, name, country):
        self.age = age
        self.name = name
        self.country = country

    def __str__(self):
        print()
        print("PERSON'S DETAILS :- ")
        print()
        return (f"The Person's Name: {name}\n"
                f"The Person's Age: {age}\n"
                f"The Person's Name: {country}\n")
    print()



print()
print("Enter Person's Details :- ")
print()
name = input ("Enter Person's Name: ")
age = int (input ("Enter Person's Age: "))
country = input ("Enter Person's Country: ")
print()

s1 = Person(name, age, country)
print(s1)