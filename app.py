from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

WEATHER_API_KEY = os.getenv('05d70bb3dfa04978c23b4989bd096b1f')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=05d70bb3dfa04978c23b4989bd096b1f&units=metric'
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return jsonify({'error': data.get('message', 'Failed to fetch weather data')}), response.status_code

    weather = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed']
    }
    return jsonify(weather)

if __name__ == '__main__':
    app.run(debug=True)
