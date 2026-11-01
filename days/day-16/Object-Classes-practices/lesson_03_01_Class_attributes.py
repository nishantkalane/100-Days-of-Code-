#class attributes are variables shared by all object of a class, unless an object overrides them with its own attribute.
class Student:
    college = "GCOEN"

    def __init__(self,name):
        self.name = name

student1 = Student("Aarav")
student2 = Student("Priya")

print(student1.college)
print(student2.college)

student3 = Student("Soukhyad")

student3.college = "Paloti"
print(student3.college)