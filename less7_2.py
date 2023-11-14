import requests
import os
from dotenv import load_dotenv


load_dotenv()


def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",  # You can change this to "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] == 200:
            temperature = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            print(f"City: {city}")
            print(f"Temperature: {temperature}°C")
            print(f"Weather: {weather}")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"Error: {e}")


def main():
    api_key = os.getenv("key")
    if api_key is None:
        print("Error: API_KEY not found in .env file.")
        return

    city = input("Enter the name of the city: ")
    get_weather(api_key, city)


if __name__ == "__main__":
    main()
