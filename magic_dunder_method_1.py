# Define a class to represent an Employee
class Employee:
    name = "Harry"  # Class-level attribute storing the employee's name
    
    # __len__ is a "dunder" (double underscore) method, also called a "magic method".
    # Dunder methods allow custom objects to work with Python's built-in functions.
    # By defining __len__, we tell Python what to return when len() is called on an Employee instance.
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i

e = Employee()
print(e.name)  # Prints "Harry"
print(len(e))  # Calls e.__len__() internally — Python "magic" translates len(e) into this dunder call