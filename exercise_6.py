# Property Deocorators

class Employee():
    raise_amount = 1.04 # Class Variable
    num_emps = 0 # Class Varibale

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + '.' + last + "@compay.com"
        Employee.num_emps += 1

    @property
    def email(self):
        # Definding email like is a method -> But it is possible to access it like an attribute
        return "{}.{}@company.com".format(self.first, self.last)
    
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee("Nicolas", "Alvarez", 50000)
emp_1.fullname = "Jim Smith"

print(emp_1.fullname)
print(emp_1.first)
print(emp_1.email)
del emp_1.fullname