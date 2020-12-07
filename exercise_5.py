# Magic / Special Methods

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

    def __repr__(self):
        # Display something that is is possible to copy and paste back in python code that would recreate that same object
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

emp_1 = Employee("Nicolas", "Alvarez", 50000)
emp_2 = Employee("Test", "User", 60000)

print(emp_1)
print(emp_1 + emp_2)
print(len(emp_1))