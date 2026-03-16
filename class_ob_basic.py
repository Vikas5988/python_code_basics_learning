# Define a class named 'person' with default attributes and a method
class person:
    name = "John"          # Default name for all instances
    job = "cloud engineer" # Default job for all instances

    def info(self):
        # Method to print the person's name and job
        print(f"{self.name} is a {self.job}")


# Create user1 using default class attributes
user1 = person()
print(f"{user1.name} is a {user1.job}")  

# Create user2 and override default attributes
user2 = person()
user2.name = "Harry"
user2.job = "Devops Engineer"
print(f"{user2.name} is a {user2.job}")  

# Create user3, override attributes, and use the info() method
user3 = person()
user3.name = "Tom"
user3.job = "AI Engineer"
user3.info()  