# List of fruits
fruits = ['apple', 'banana', 'cherry', 'date']

print("Using enumerate():")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
    
print("Using enumerate without index")
for index, fruit in enumerate(fruits):
    print(f"{fruit}")
    
    print("Using enumerate default index")
for items in enumerate(fruits):
    print(f"{items}")

print("\nWithout enumerate():")
index = 0
for fruit in fruits:
    print(f"Index {index}: {fruit}")
    index += 1