class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    @ property
    def email (self):
        return "{}.{}@email.com".format(self.first, self.last)
    @ property
    def fullname(self):
        return "{}, {}".format(self.first, self.last)

emp_1= Employee("Alexander", "Nepomnyashchii")
emp_2= Employee("Michael", "Mirkin")
emp_1.first ="Jim"
print(emp_1.email)
print(emp_1.first)
print(emp_1.fullname)
#class, method, instance