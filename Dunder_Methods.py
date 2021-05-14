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

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)

    def __str__(self):
        return '{}-{}'.format(self.fullname(),self.email)

    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp1=Employee("Ridhima","Chopra",100000)
emp2=Employee("Aashna","Chopra",100000)

#print(repr(emp1))
#print(str(emp1))

#print(emp1+emp2)

print(len(emp2))