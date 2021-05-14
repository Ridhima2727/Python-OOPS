class Employee:
    raise_amount=1.04
    num_emp=0

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+"."+last+"@company.com"

        Employee.num_emp+=1     #since number of employees isnt specific to any one instance
    
    def fullname(self):
        return self.first+" "+self.last

    def apply_raise(self):
       self.pay= int(self.pay*self.raise_amount)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay=emp_str.split("-")
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day): #mon=0,tues=1,wed=2,thurs=3... and so on
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

#print(Employee.num_emp)                                   #ans =0; no employee assigned yet

emp1=Employee("Ridhima","Chopra",100000)
emp2=Employee("Aashna","Chopra",100000)

#print(emp1.fullname()) #one way
#print(Employee.fullname(emp1)) #another way

#print(emp1.pay)
#emp1.apply_raise()
#print(emp1.pay)

'''
emp1.raise_amount=1.04                     #sets raise amount to 1.04 for the entire class
emp1.raise_amount=1.04
Employee.raise_amount=1.05       #sets the raise amount to 1.05 only for the instance 1.05


Employee.set_raise_amt(1.05)                         #setting raise amount for entire class

print(emp1.raise_amount)                    #sets raise amount to 1.04 for the entire class
print(emp1.raise_amount)
print(Employee.raise_amount)
#print(Employee.num_emp)


emp3=Employee.from_string("Sai_Aasrith-Avvaru-100000")

print(emp3.email)
print(emp3.pay)
'''


import datetime
my_date = datetime.date(2021,3,13)    #yyyy-mm-dd
print(Employee.is_workday(my_date))