# Use of Self?

# Without Self
class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

emp_1.first = 'Saurabh'
emp_1.last = 'Kumar'
emp_1.email = 'Saurabh.Kumar@gmail.com'
emp_1.pay = 10000

emp_2.first = 'Sneha'
emp_2.last = 'Sharma'
emp_2.email = 'Sneha.Sharma@gmail.com'
emp_2.pay = 10000

print(emp_1.email)
print(emp_2.email)

##################################################################

# With Self
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print('{} {}'.format(emp_1.first, emp_1.last)) # Without creating function
print(emp_1.fullname())

###################################################################

# Without Self in fullname method What will happen?

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname():
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.fullname())
# ERROR: fullname() takes 0 positional arguments but 1 was given. We should pass self.

#######################################################################

# Other ways of passing an object in a class

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.fullname()) # here attribute is called using object, by default self is there
print(Employee.fullname(emp_1)) # here object is passed in class, self is not default
