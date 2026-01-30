def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n - 1)

# Taking input from the user
n = int(input("Enter a number: "))

# Function call
result = sum_natural(n)

print("Sum of first", n, "natural numbers is:", result)
