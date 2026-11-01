#A class mehtod works eith the class itself rather than a particular object's data.
# It usees cls as its first parameter and the @classmethod decorator

class Student:
    college = "GCOEN"
    def __init__(self,name):
        self.name = name

    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college

s1 = Student("Arav")
s2 = Student("Priya")

print(s1.college)
Student.change_college("IIT Bombay")
print(s1.college)
print(s2.college)

# When do we use class methods?
# - Modifying class-level data.
# - Creating alternative ways to construct objects.
# - Working with data shared by all instances.