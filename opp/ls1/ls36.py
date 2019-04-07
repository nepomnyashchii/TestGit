class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def email (self):
        return "{}.{}@email.com".format(self.first, self.last)

    def fullname(self):
        return "{}, {}".format(self.first, self.last)

emp_1= Employee("Alexander", "Nepomnyashchii")
emp_2= Employee("Michael", "Mirkin")
emp_1.first ="Jim"
print(emp_1.email())
print(emp_1.fullname())
print(emp_1.first)
#class, method, instance
