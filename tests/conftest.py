import os
import responses
import pytest
from app import app as flask_app
import json
with open('./test_data.json', 'r') as myfile:
  data=myfile.read()
api_data = json.loads(data)

@pytest.fixture
def app():
  yield flask_app

@pytest.fixture
def client(app):
  lat = 33.441792
  lon = -94.037689

  api_key = os.getenv("API_KEY")

  responses.add(responses.GET,
    f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly&appid={api_key}',
    json=api_data,
    status=200
  )

  app.config['TESTING'] = True
  client = app.test_client() 

  yield client