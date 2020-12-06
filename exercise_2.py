# Class Variables

class Employee():
    raise_amount = 1.04 # Class Variable
    num_emps = 0 # Class Varibale

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@compay.com"
        Employee.num_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.num_emps)

emp_1 = Employee("Nicolas", "Alvarez", 50000)
emp_2 = Employee("Test", "User", 60000)

print(Employee.num_emps)

emp_1.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
