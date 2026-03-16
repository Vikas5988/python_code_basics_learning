# Define a class named 'person' with a constructor and an instance method
class Person:
    
    def __init__(self, username, occupation):
        # Constructor: called automatically when a new instance is created
        print("Printing user info")
        self.name = username    # Assign username to instance attribute 'name'
        self.job = occupation   # Assign occupation to instance attribute 'job'

    def info(self):
        # Display the name and job of the person instance
        print(f"{self.name} is a {self.job}")

# Create an instance user1 with name and occupation passed as arguments
user1 = Person("Mike", "Network Engineer")
user1.info()  # Call info() on user1

# Create an instance user2 with different name and occupation
user2 = Person("Bala", "Manager")
user2.info()  # Call info() on user2