'''
Difference between Instance Variable and Class Variable ?
How to change a regular method to a class method ?
A regular method is the one which takes self as a 1st argument, where as a 
class method takes class as an 1st argument. This can be acheived by adding
@classmethod on top of any method know as decorator.

Just like instance is called by self, class is called by cls

Self Method: Passes self as argument
Class Method - Passes cls as argument
Static Method - Passes nothing as argument'''

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay*1.04) # 4% can be made a class variable
        
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# Class Variable

class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        # raise_amount can be accessed only by passing class name or self to it.
        # self.raise_amount, or Employee.raise_amount
        
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Updating raise amount using class
# Employee.raise_amount = 1.05
'''In this only raise amount related to both emp_1, 2 are changed'''
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# Updating raise amount using class
'''In this only raise amount related to emp_1 is changed'''
emp_1.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

'''Above concept palys imp role as func apply_raise will give different results
if we apply self or Employee to it'''

############################################################################

'''Example of a case where self will not make sense. Creating no of employees and class
varaible and incrementing it as we add more employees as object.'''

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

print('Method 1')
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee(first, last, pay)
print(new_emp_1.first)
print(new_emp_1.last)
print(new_emp_1.pay)
print(new_emp_1.email)

print('\nMethod 2')
new_emp_2 = Employee.from_string(emp_str_2)

print(new_emp_2.first)
print(new_emp_2.last)
print(new_emp_2.pay)
print(new_emp_2.email)

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))