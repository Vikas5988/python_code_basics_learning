class Employee:
    def __init__(self,emp_name,emp_salary):
        self.name = emp_name
        self.salary = emp_salary
        
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])
    

emp1 = Employee("Frank",15000)
print(emp1.name,emp1.salary)

string = "John-12000"
emp2 = Employee(string.split("-")[0],string.split("-")[1])

print(emp2.name,emp2.salary)

string2 = "Harry-22000"

emp3 = Employee.fromStr(string2)

print(emp3.name,emp3.salary)