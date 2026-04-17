# Compare: Generator vs Normal Function
# -------- Generator Function --------
def gen_count():
    for i in range(5):
        yield i          # Gives one value at a time

# -------- Normal Function --------
def list_count():
    numbers = []

    for i in range(5):
        numbers.append(i)   # Store all values in list first
    return numbers          # Return complete list

# -------- Using Generator --------
print("Using Generator (values come one by one):")

for num in gen_count():
    print("Generator Value =", num)

# -------- Using Normal Function --------
print("\nUsing Normal Function (all values stored first):")

for num in list_count():
    print("List Value =", num)