# Define a class to represent an Employee
class Employee:
    name = "Harry"

    # __str__ is a dunder/magic method called when str() or print() is used on an object.
    # It returns a human-readable string representation of the object.
    def __str__(self):
           return f"The name of the employee is {self.name} str"

    # __repr__ is a dunder/magic method called when repr() is used on an object.
    # It returns an unambiguous, developer-friendly representation — ideally enough to recreate the object.
    def __repr__(self):
        return f"Employee('{self.name}')"

    # __call__ is a dunder/magic method that makes an instance callable like a function.
    # When you do e(), Python internally calls e.__call__().
    def __call__(self):
        print("Hey I am good")


e = Employee()

print(str(e))   # Triggers __str__  → "The name of the employee is Harry str"
print(repr(e))  # Triggers __repr__ → "Employee('Harry')"
e()             # Triggers __call__ → "Hey I am good"