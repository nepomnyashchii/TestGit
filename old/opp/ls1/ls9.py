class Employee:
    raise_amount = 1.10
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"

    def fullname(self):
        return "{}, {}".format(self.first, self.last)
    def apply_raise (self):
        self.pay = int(self.pay*self.raise_amount)

emp_1= Employee("Alexander", "Nepomnyashchii", 60000)
emp_2= Employee("Michael", "Mirkin", 50000)
print(emp_1.__dict__)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)