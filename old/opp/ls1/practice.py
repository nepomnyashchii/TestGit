class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"


class Developer(Employee):
    def __init__(self, first, last, pay, language):
        super().__init__(first, last, pay)
        # Employee.__init__(self,first,last,pay)
        self.language = language


dev_1 = Developer("Alexander", "Nepomnyashchii", "60000", "Python")
print(dev_1.first)
print(dev_1.language)
