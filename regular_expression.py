import re

text = """
John Smith was born on 1990-05-15. His email is john.smith@gmail.com
and his phone number is 123-456-7890. He lives at 742 Evergreen Street,
New York. His zip code is 10001.
"""

# Extract dates
dates = re.findall(r'\d{4}-\d{2}-\d{2}', text)
print("Dates:   ", dates)

# Extract email
email = re.findall(r'\w+\.\w+@\w+\.\w+', text)
print("Email:   ", email)

# Extract phone number
phone = re.findall(r'\d{3}-\d{3}-\d{4}', text)
print("Phone:   ", phone)

# Extract zip code
zipcode = re.findall(r'\b\d{5}\b', text)
print("Zip Code:", zipcode)

# Extract name (two capitalized words)
name = re.findall(r'[A-Z][a-z]+\s[A-Z][a-z]+', text)
print("Name:    ", name)