class Employee:
    # Class variable shared across all instances
    company = "Google"

    def show(self):
        # Display the employee's name and their associated company
        print(f"Employee name is {self.name} and working in {self.company}")

    @classmethod
    def changeCompany(cls, new_compnay_name):
        # Update the class-level company variable for all instances
        cls.company = new_compnay_name


# Create an instance of Employee
emp1 = Employee()

# Assign an instance variable 'name' dynamically
emp1.name = "Mike"

# Display employee info before company change
emp1.show()

# Change the company for all Employee instances via class method
emp1.changeCompany("Facebook")

# Display employee info after company change
emp1.show()

# Access the updated class variable directly from the class
print(Employee.company)