def print_multiplication_table(number):
    """Prints the multiplication table of the given number."""
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Example usage
num = int(input("Enter a number to print its multiplication table: "))
print_multiplication_table(num)