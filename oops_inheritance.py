# Base class representing a general Employee
class Employee:
    def __init__(self, emp_name, emp_id):
        # Store the employee's ID and name as instance attributes
        self.employee_ID = emp_id
        self.employee_name = emp_name
    
    def show_detail(self):
        # Display the employee's ID and name
        print(f"The name of the Employe {self.employee_ID} is {self.employee_name}")

# Subclass that inherits from Employee, representing a Developer role
class Developer(Employee):
    def show_role(self):
        # Display the specific role of this employee
        print("User is working as Developer")


# Create an Employee instance (base class — has no show_role method)
emp1 = Employee("Ramesh", "112233")

emp1.show_detail()       # Works: show_detail() is defined in Employee
# emp1.show_role()       # AttributeError: Employee has no show_role() method

# Create a Developer instance (subclass — inherits show_detail, adds show_role)
emp2 = Developer("Dev", "2343")
emp2.show_detail()       # Works: inherited from Employee
emp2.show_role()         # Works: defined in Developer