# MAP Function - map() applies a function to every item in an iterable

# Function to calculate the cube of a number
def cube(x):
    return x * x * x

# Test the cube function with a single value
print(cube(4))

# Original list of numbers to process
list_original = [2, 5, 7, 4, 3, 4, 6, 5]
new_list = []

# Manual approach: using a for loop to apply cube() to each element
for item in list_original:
    new_list.append(cube(item))

print(new_list)

# Using map() to apply cube() to every element in list_original
# map() returns a map object (lazy iterator), not a list directly
new_list_map = []
new_list_map = map(cube, list_original)

# map() returns a map object — wrap with list() to see the values
print("Type of new list by Map :", new_list_map)
print("New List by Map :", list(new_list_map))


# FILTER Function - filter() keeps only items where the function returns True

# Function returns True if the value is greater than 3
def filter_function(a):
    return a > 3

# Apply filter to list_original — only elements > 3 are kept
new_list_filter = list(filter(filter_function, list_original))

print("New List by Filter Function :", new_list_filter)


# REDUCE Function - reduce() repeatedly applies a function to collapse a list to a single value
from functools import reduce  # reduce is not built-in; must be imported

numbers_list = [1, 2, 3, 4, 5]

# Function to add two numbers together
def mysum(x, y):
    return x + y

# reduce applies mysum cumulatively: ((((1+2)+3)+4)+5) = 15
sum = reduce(mysum, numbers_list)

print(sum)