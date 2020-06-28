'''
https://www.youtube.com/watch?v=jCzT9XFZ5bw&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=6
'''

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')
emp_1.fullname = "Corey Schafer"

print('Using email as class method rather than passing it in self like other examples')
print(emp_1.first)
print(emp_1.email()) # The paranthesis need to be added. If we delete is we get error
print(emp_1.fullname)


############################################
# To remove parathesis, need to type @property
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter # this sets both first name, last name, and email
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
emp_1.fullname = "Corey Schafer"

print(emp_1.first)
print(emp_1.email) # without paranthesis
print(emp_1.fullname) # setting @ property to call fullname without parathesis i.e. ()

del emp_1.fullname