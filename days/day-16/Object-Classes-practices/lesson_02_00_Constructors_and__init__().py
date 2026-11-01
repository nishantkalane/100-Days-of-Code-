# instead of creating a object and then passing the attributes by creating them each time we pass them while creating the object that will be better

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age


student1 = Student("Arnav", 13)
student2 = Student("CJ",29)

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.name)