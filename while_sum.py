# Get input from user
n = int(input("Enter a positive integer: "))

# Initialize variables
sum_total = 0
counter = 1

# Calculate sum using while loop
while counter <= n:
    sum_total += counter
    counter += 1

# Display result
print("The sum of first", n, "natural numbers is:", sum_total)
