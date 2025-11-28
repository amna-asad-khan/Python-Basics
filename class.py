class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age 


n = input("Enter name: ")
a = int(input("Enter age: "))
o = Person(n, a)
print(o.name, o.age)
    
