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

class Developer(Employee):
    raise_amount=1.10

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay,employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("-->",emp.fullname())
        


dev1=Developer("Ridhima","Chopra",100000,"Python")
dev2=Developer("Aashna","Chopra",100000,"Java")
dev3=Developer("Sai_Aasrith","Avvaru",10000,"C/C++")

mgr1=Manager("Sanchari","Mahanti",100000,[dev1])

print(mgr1.email)

mgr1.add_emp(dev2)
mgr1.remove_emp(dev1)
mgr1.print_emp()

'''
print(dev1.prog_lang)
print(dev2.prog_lang)
print(dev3.prog_lang)
 

print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)
'''