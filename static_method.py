
# A class to perform basic math operations on a number
class Math:
    def __init__(self, number):
        self.num = number  # Store the initial number as an instance attribute

    def addtonum(self, new_num):
        self.num = self.num + new_num  # Add new_num to the current number

    @staticmethod
    def add(a, b):
        return a + b  # Return the sum of two numbers (no instance needed)


a = Math(8)       # Create a Math object with initial value 8
print(a.num)      # Output: 8

a.addtonum(11)    # Add 11 to a.num (8 + 11 = 19)
print(a.num)      # Output: 19

print(a.add(22, 33))    # Call static method via instance — Output: 55
print(Math.add(33, 44)) # Call static method via class — Output: 77
