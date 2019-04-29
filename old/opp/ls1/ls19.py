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

    # @classmethod
    # def from_string (cls, emp_str):
    #     first, last, pay = emp_str_1.split("-")
    #     return cls(first, last, pay)
    @staticmethod
    def is_workday (day):
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        return True

import datetime
my_date = datetime.date (2019, 4, 3)

print(Employee.is_workday(my_date))
