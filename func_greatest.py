def greatest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Taking input from the user
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

# Function call
greatest = greatest_of_three(x, y, z)

print("Greatest number is:", greatest)
