import os
from flask import Flask, jsonify
import requests
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
if __name__ == '__main__':
  app.run(debug=True)

@app.route('/', methods=['GET'])
def home():
  return jsonify({'hello': 'world'})

@app.route('/forcast', methods=['GET', "POST"])
def get_forcast():
  if request.method == "POST":
    lat = request.form['city']
    lon = request.form['country']
    api_key = os.getenv("API_KEY")
    weather_url = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly&appid=e7b8d42f2fca6e9f0e129a23c6368d0e')

    weather_data = weather_url.json()

    temp = round(weather_data['main']['temp'])
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
