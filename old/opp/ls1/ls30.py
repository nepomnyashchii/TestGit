class Employee:
    raise_amt = 1.20
    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    def apply_raise (self):
        self.pay = int(self.pay*self.raise_amt)     
class Developer (Employee):
#     pass
# dev_1 = Employee("Alexander", "Nepomnyashchii", 80000)
# print (dev_1.pay)
# dev_1.apply_raise ()
# print(dev_1.pay)
    raise_amt = 10
# dev_1 = Employee("Alexander", "Nepomnyashchii", 80000)
# print (dev_1.pay)
# dev_1.apply_raise ()
# print(dev_1.pay)
# # no change 
dev_1 = Developer("Alexander", "Nepomnyashchii", 80000)
print (dev_1.pay)
dev_1.apply_raise ()
print(dev_1.pay)
# change     
