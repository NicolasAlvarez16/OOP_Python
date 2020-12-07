# Inheritance

class Employee:
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

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_lan):
        super().__init__(first, last, pay)
        self.prog_lan = prog_lan

class Manager(Employee):
    # It not good practices to pass mutable data types as defaul argumets --> employees = None
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp is not self.employees:
            self.employees.append(emp)
    
    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())

dev_1 = Developer("Nicolas", "Alvarez", 50000, "Python")
dev_2 = Developer("Test", "User", 60000, "C")

mgr_1 = Manager('Sue', "Smith", 90000, [dev_1])
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.rem_emp(dev_1)
mgr_1.print_emps()

# print(isinstance(mgr_1, Developer))
# print(issubclass(Manager, Developer))

# print(dev_1.email)
# print(dev_1.prog_lan)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)