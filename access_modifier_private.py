class Employee:
    def __init__(self):
        # Private attribute using name mangling (double underscore prefix)
        # Accessible externally as _Employee__name, not directly as __name
        self.__name = "First Employee"

emp1 = Employee()

# This would raise AttributeError because __name is name-mangled
# print(emp1.name)

# Accessing the private attribute using Python's name mangling syntax: _ClassName__attribute
print(emp1._Employee__name)