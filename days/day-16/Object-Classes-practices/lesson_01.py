class Student:
    pass

student1 = Student()
student2 = Student()

# instances of student were created (objects) at a location which are referenced
# by the variables student1 and student2

print(student2)
print(student1)

# attributes: giving objects their own data
# One way of creating and assigning attribute, i.e associate the attribute with the object referecend by student1 and assigns the value "Arnav"

student1.name = "Arnav"
student1.age = 16

student2.name = "Akshay"
student2.age = 22

#printing attributes
print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)

student1.name ="Nishant"
print(student1.name)

#(above way of declaring attribute is not the best way we will learn a better way in future

student2.age = 23
print(student2.age)


# print(student1.marks) attribute wasn't declared, error: AttributeError: 'Student' object has no attribute 'marks'