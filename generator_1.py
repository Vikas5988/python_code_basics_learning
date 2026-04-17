# Generator function
def numbers():
    yield 1
    yield 2
    yield 3

# Create generator object
x = numbers()


print(next(x))   # First value
print(next(x))   # Second value
print(next(x))   # Third value