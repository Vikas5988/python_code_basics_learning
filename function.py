
# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    if not numbers:  # Check if the list is empty
        return 0
    return sum(numbers) / len(numbers)

# Example usage of the calculate_average function
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("The average of the list is:", average)


#create a fucntion which add two numbers
def add_two_numbers(a, b):
    return a + b
# Example usage of the add_two_numbers function
num1 = 5
num2 = 10
result = add_two_numbers(num1, num2)
print("The sum of", num1, "and", num2, "is:", result)