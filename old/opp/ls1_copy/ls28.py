class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"
class Developer (Employee):
    pass
# dev_1= Employee("Alexander", "Nepomnyashchii", 60000)
# dev_2= Employee("Michael", "Mirkin", 50000)
dev_1= Developer("Alexander", "Nepomnyashchii", 60000)
dev_2= Developer("Michael", "Mirkin", 50000)
print(dev_1.email)
print(dev_2.last)
