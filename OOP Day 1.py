# OOP Python

class Employee:
    # this function initializes the program
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# both of these work exactly the same
emp_1.fullname()
Employee.fullname(emp_1)

# print(emp_1.email)
# print(emp_2.email)

# print(emp_1.fullname())

"""This code segment is an inefficient way of doing this
emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 60000
"""


class CAT:

    def __init__(self, furtype, furcolor, gender):
        self.furtype = furtype
        self.furcolor = furcolor
        self.gender = gender

    def catID(self):
        if self.gender == 'male':
            genID = 'he'
        else:
            genID = 'she'
        return genID + ' is a ' + self.furtype + " " + self.furcolor + ' cat!'


pika = CAT('short', 'tabby', 'male')

print(pika.catID())
print(CAT.catID(pika))