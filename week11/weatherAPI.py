import requests

# 1. Define the URL (the endpoint)
url = "https://api.open-meteo.com/v1/forecast"

# 2. Define your parameters (Berlin in this case)
params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "current_weather": True
}

# 3. Make the "GET" request
response = requests.get(url, params=params)

# 4. Check if it worked (Status Code 200 means Success)
if response.status_code == 200:
    # 5. Parse the JSON data into a Python dictionary
    data = response.json()
    
    temp = data["current_weather"]["temperature"]
    wind = data["current_weather"]["windspeed"]
    
    print(f"The current temperature in Berlin is {temp}°C.")
    print(f"Wind speed: {wind} km/h.")
else:
    print(f"Error: {response.status_code}")