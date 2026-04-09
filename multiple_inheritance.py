# A child class inherits from MORE THAN ONE parent class
# FIRST PARENT CLASS
class Father:
    
    def __init__(self):
        self.father_name = "John"      # Father's own attribute
    
    def gardening(self):
        print("Father loves gardening.")
    
    def cooking(self):
        print("Father can cook basic meals.")

# SECOND PARENT CLASS
class Mother:
    
    def __init__(self):
        self.mother_name = "Mary"      # Mother's own attribute
    
    def painting(self):
        print("Mother loves painting.")
    
    def cooking(self):                 # Same method name as Father!
        print("Mother can cook delicious meals.")


# CHILD CLASS inheriting from BOTH Father and Mother
# Syntax: class Child(Parent1, Parent2)
class Child(Father, Mother):
    
    def __init__(self):
        Father.__init__(self)          # Initialize Father's attributes
        Mother.__init__(self)          # Initialize Mother's attributes
        self.name = "Alex"             # Child's own attribute
    
    def playing(self):                 # Child's own method
        print(f"{self.name} loves playing football.")


# -------USAGE-------

child = Child()                        # Creates Child object

# Child can access BOTH parents' attributes
print(f"Father's name: {child.father_name}")
print(f"Mother's name: {child.mother_name}")
print(f"Child's name : {child.name}")

print()

# Child can call BOTH parents' methods
child.gardening()      # Inherited from Father
child.painting()       # Inherited from Mother
child.playing()        # Child's own method

print()

# CONFLICT: Both Father and Mother have cooking()
# Python follows MRO (Method Resolution Order) — left to right
# Since Father is written first in Child(Father, Mother), Father's cooking() is called
child.cooking()

print()

# MRO shows the order Python searches for methods
# Output: Child -> Father -> Mother -> object
print(f"MRO Order: {[cls.__name__ for cls in Child.__mro__]}")