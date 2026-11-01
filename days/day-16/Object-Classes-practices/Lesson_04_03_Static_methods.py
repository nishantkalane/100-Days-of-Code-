# A static method is a method placed inside a class that does not need access to either the object (self) or the class (cls).
class Student:
    @staticmethod
    def is_asdult(age):
        return age >= 18

student1 = Student()

#calling through the class
print(Student.is_asdult(21))

#calling through the object
print(student1.is_asdult(22))



# #What's happening?
# 1. @staticmethod tells Python that this method doesn't need an automatically passed object or class.
# 2. is_adult(age) receives only the age argument.
# 3. It checks whether the age is 18 or above.
# 4. It returns True or False.

# When do we use static methods?
#
# When a function is logically related to a class but doesn't need its object or class data.