class Employee:
    raise_amount = 1.10
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)
    def apply_raise (self):
        self.pay = int(self.pay*self.raise_amount)

    def __repr__ (self):
        return "Employee ('{}', '{}', {}) ".format(self.first, self.last, self.pay)
    def __str__ (self):
        return '{} - {}'.format(self.fullname(), self.email)
    def __add__(self, other):
        return self.pay + other.pay
    def __len__(self):
        return len(self.fullname())
emp_1= Employee("Alexander", "Nepomnyashchii", 60000)
emp_2= Employee("Michael", "Mirkin", 50000)
print(len(emp_1))