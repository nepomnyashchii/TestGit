class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"
emp_1= Employee("Alexander", "Nepomnyashchii", 60000)
emp_2= Employee("Michael", "Mirkin", 50000)
print(emp_2.email)
print(emp_1.last)