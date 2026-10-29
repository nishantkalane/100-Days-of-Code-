class Student:
    def introduce(self):
        # def defines a
        # function.
        #
        # introduce is the method name.
        #
        # self is the
        # conventional name for the first parameter of an instance method.
        print("Hello I am student")

student1 = Student()
student2 = Student()

#The first accesses the bound method without calling it. The second calls it.
student1.introduce
student1.introduce()
student2.introduce()