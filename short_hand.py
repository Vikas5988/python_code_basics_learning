# Basic syntax: value_if_true if condition else value_if_false

# Example 1: Check if number is even or odd
num = 8
result = "Even" if num % 2 == 0 else "Odd"
print(result)  # Output: Odd

# Example 2: Find maximum of two numbers
a = 15
b = 20
maximum = a if a > b else b
print("Maximum:", maximum)  # Output: Maximum: 20

# Example 3: Check pass or fail
score = 55
status = "Pass" if score >= 75 else "Fail"
print(status)  # Output: Pass