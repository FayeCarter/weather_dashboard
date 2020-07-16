import os
from flask import Flask, jsonify, request
import requests
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
if __name__ == '__main__':
  app.run(debug=True)

@app.route('/', methods=['GET'])
def home():
  return jsonify({'hello': 'world'})

@app.route('/forcast', methods=["GET"])
def get_forcast():
  query_parameters = request.args
  lat = query_parameters.get('lat')
  lon = query_parameters.get('lon')

  api_key = os.getenv("API_KEY")
  weather_url = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly&appid={api_key}')

  weather_data = weather_url.json()

  response = {
    "current": weather_data['current'],
    "daily": weather_data['daily']
  }

  return jsonify(response)
