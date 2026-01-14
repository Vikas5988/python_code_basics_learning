#Write a function with recursion which give factorial of a number
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
#It should ask input from user without try, while and except
def get_input():
    n = input("Enter a non-negative integer to calculate its factorial: ")
    if n.isdigit():
        return int(n)
    else:
        print("Invalid input. Please enter a non-negative integer.")
        return get_input()
# Call the functions
number = get_input()
result = factorial(number)
print(f"The factorial of {number} is {result}")