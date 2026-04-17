import requests

# Send request to a website
response = requests.get("https://example.com", verify=False)

# Print status code
print("Status Code:", response.status_code)

# Print first 100 characters of response
print("Data:", response.text[:100])