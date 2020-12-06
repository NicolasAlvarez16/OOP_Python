# Introduction to Classes

class Employee():
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay  = pay
        self.email = first + '.' + last + "@company.com" 

    def full_name(self):
        return "{} {}".format(self.first, self.last)


emp_1 = Employee("Nicolas", "Alvarez", 50000)
emp_2 = Employee("Test", "User", 60000)

# print(emp_1)
# print(emp_2)

emp_1.raise_amount = 1.04
print(emp_1.email)
print(emp_2.email)
print(emp_1.full_name())