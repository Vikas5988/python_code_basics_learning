# List of fruits
fruits = ['apple', 'banana', 'cherry', 'date']

print("Using enumerate():")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

print("\nWithout enumerate():")
index = 0
for fruit in fruits:
    print(f"Index {index}: {fruit}")
    index += 1