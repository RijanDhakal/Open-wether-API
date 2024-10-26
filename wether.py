import requests

def get_weather():
    city_name = input("Enter City Name: ")
    API_Key = "1bd1404eaabf8731d7c6b7bcea736636"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        result = (
            f"Country: {data['sys']['country']}, {city_name}\n"
            f"Status: {data['weather'][0]['description']}\n"
            f"Temperature: {data['main']['temp']}°C\n"
            f"Feels like: {data['main']['feels_like']}°C\n"
            f"Humidity: {data['main']['humidity']}%"
        )
        print(result)
    else:
        print(f"Error: PLACE NOT FOUND | Status Code: {response.status_code} | TRY AGAIN LATER")

# Run the weather function
get_weather()
