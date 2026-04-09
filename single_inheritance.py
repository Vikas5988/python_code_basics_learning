# PARENT CLASS (also called Base Class or Super Class)
class Animal:
    # Constructor of parent class
    def __init__(self, name):
        self.name = name          # Instance variable shared with child class

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

# CHILD CLASS (also called Derived Class or Sub Class)
# Dog inherits everything from Animal by passing it in parentheses
class Dog(Animal):
    
    # Child class has its own constructor with extra attribute 'breed'
    def __init__(self, name, breed):
        
        # Manually calling parent constructor to initialize 'name'
        # Without this line, self.name would not be set and eat()/sleep() would crash
        Animal.__init__(self, name)
        
        self.breed = breed        # Extra attribute only Dog has, Animal doesn't know about this

    # This method belongs only to Dog, Animal does not have it
    def bark(self):
        print(f"{self.name} says: Woof!")


# -------USAGE-------

dog = Dog("Buddy", "Labrador")  # Creates a Dog object with name and breed

dog.eat()        # Inherited from Animal — Dog didn't define this, but can still use it
dog.sleep()      # Inherited from Animal — same as above
dog.bark()       # Dog's own method — only Dog can call this, not Animal

print(f"Breed: {dog.breed}")                           # Dog's own attribute
print(f"Dog's parent class: {Dog.__bases__[0].__name__}")  # Shows 'Animal' — confirms inheritance