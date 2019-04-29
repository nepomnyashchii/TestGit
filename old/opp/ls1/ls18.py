class Employee:
    # num_of_emps =0
    # raise_amt = 1.10
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"
        # Employee.num_of_emps +=1

    # def fullname(self):
    #     return "{}, {}".format(self.first, self.last)
    # def apply_raise (self):
    #     self.pay = int(self.pay*self.raise_amount)

    # @classmethod
    # def set_raise_amt (cls, amount):
    #     cls.raise_amt = amount

    @classmethod
    def from_string (cls, emp_str):
        first, last, pay = emp_str_1.split("-")
        return cls(first, last, pay)

# emp_1= Employee("Alexander", "Nepomnyashchii", 60000)
# emp_2= Employee("Michael", "Mirkin", 50000)

emp_str_1 = "Alexander - Nepomnyashchii -80000"
emp_str_2 = "Michael - Mirkin -90000"
emp_str_3 = "Elena - Goldin -50000"

new_emp_1 = Employee.from_string(emp_str_1)

print (new_emp_1.last)
print (new_emp_1.email)

