class Employee:
    def __init__(self,name,age,salary, department = "General"):
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department

    def display_Details(self):
        print(f"Employee Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")

emp1 = Employee("Arav",25,35000,"IT")

epm2 = Employee("Priya",27,45000, "HR")


emp1.display_Details()
print()
epm2.display_Details()
print()
#employee without department:
epm3 = Employee("Nish",23,500000)

epm3.display_Details()