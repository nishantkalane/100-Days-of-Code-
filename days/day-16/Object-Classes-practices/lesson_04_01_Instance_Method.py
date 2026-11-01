class Student:
    def __init__(self,name,age):
        self.name =name
        self.age = age
    def introduce(self):
        print(f"Hii, my name is {self.name}")
        print(f"My age is {self.age}")

s1 = Student("Niki",21)
s2 = Student("Nick",18)

# An instance method is a method that works with a particular object
# It uses self as its first parameter.
s1.introduce()
print()
s2.introduce()

# When do we use instance methods?
# When a method needs to access or modify an individual object's attributes.