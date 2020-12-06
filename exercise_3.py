# Class Methods and Static Methods

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
    
    @classmethod
    def set_raise_amt(cls, amount):
        # cls -> class, Working with the class instead of the instance
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')    
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        # Static method -> instance or the class is not accessed anywhere within the method
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee("Nicolas", "Alvarez", 50000)
emp_2 = Employee("Test", "User", 60000)

'''USING CLASS METHODS'''
# emp_str_1 = "John-Doe-70000"
# emp_str_2 = "Steve-Smith-30000"
# emp_str_3 = "Jane-Doe-90000"

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

'''USING STATIC METHODS'''
import datetime
my_date = datetime.date(2020, 7, 11)
print(Employee.is_workday(my_date))