
import requests

API_KEY = '885b6946e52a1bae8c6177c13cca6143'

def get_weather(location):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'condition': data['weather'][0]['description'],
            'wind': data['wind']['speed']
        }
    return {'error': 'Could not fetch weather data'}
