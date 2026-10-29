class Students:
    def introduce(self):
        print(f"Hii my name is {self.name}")


student1 = Students()
student2 = Students()

student1.name = "Arnav"
student2.name = "Yatharth"

student1.introduce()
student2.introduce()

# ## Python `self` 💡
#
# - `self` refers to the current object whose method is being called.
# - It allows methods to access that object's attributes and other methods.
# - Python automatically passes the object as the first argument when you call an instance method.
# - `self` is a convention, not a Python keyword.
#
# Remember: `self.name` means the `name` belonging to the current object.
#
# Conceptually, `student1.introduce()` passes `student1` as `self`, while `student2.introduce()` passes `student2`.