def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

# Taking input from the user
celsius = float(input("Enter temperature in Celsius: "))

# Function call
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius}°C is equal to {fahrenheit}°F")