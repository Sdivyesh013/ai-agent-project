import requests

# Ask a website for data
response = requests.get("https://api.github.com/zen")

# Show what came back
print("Status code:", response.status_code)
print("Message:", response.text)