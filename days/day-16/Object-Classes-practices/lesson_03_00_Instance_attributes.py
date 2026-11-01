#instance attributes student1.name, student2.name, one won't change other
class Student:
    def __init__(self,name, age):
        self.name = name
        self.age = age

student1 = Student("Arav",21)
student2 = Student("Priya",22)

print(student1.name)
print(student2.name)