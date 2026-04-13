# Multilevel Inheritance in Python
# A -> B -> C (each class inherits from the one above)

# Base class (Grandparent)
class Animal:
    def __init__(self, name):
        self.name = name  # Instance variable

    def eat(self):
        print(f"{self.name} is eating.")

    def breathe(self):
        print(f"{self.name} is breathing.")

# Child class (Parent) — inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # Call Animal's __init__
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")

# Grandchild class — inherits from Dog (and indirectly from Animal)
class Puppy(Dog):
    def __init__(self, name, breed, age_months):
        super().__init__(name, breed)   # Call Dog's __init__
        self.age_months = age_months

    def play(self):
        print(f"{self.name} ({self.age_months} months old) is playing!")

# ------- Main Program -------

puppy = Puppy("Buddy", "Labrador", 3)

puppy.breathe()       # Inherited from Animal (grandparent)
puppy.eat()           # Inherited from Animal (grandparent)
puppy.bark()          # Inherited from Dog (parent)
puppy.play()          # Defined in Puppy (own method)

# Check the inheritance chain
print(Puppy.__mro__)  # Method Resolution Order