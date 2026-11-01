from typing import SupportsAbs


class Student:
    def __init__(self,name,age,course,club="Not Assigned"):
        self.name = name
        self.age = age
        self.course = course
        self.club =club

    def introduce(self):
        print(f"Hii my name is {self.name}")
        print(f"My age is {self.age}")
        print(f"I am enrolled in course of {self.course}")
        print(f"I am in club: {self.club}")

student1 = Student("jhon",23,"Civil Engineering")
student2 = Student("nish",23,"Computer Science Engineering","SAB")

student1.introduce()
print()
student2.introduce()

student3 = Student()