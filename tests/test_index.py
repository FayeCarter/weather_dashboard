import json
import responses
with open('./response_data.json', 'r') as myfile:
  data=myfile.read()

response_data = json.loads(data)

def test_index(app, client):
  del app
  res = client.get('/')
  assert res.status_code == 200
  expected = {'hello': 'world'}
  assert expected == json.loads(res.get_data(as_text=True))

@responses.activate
def test_forecast(app, client):
  del app
  response = client.get('/forcast?lat=33.441792&lon=-94.037689')
  assert response.status_code == 200
  assert response.json == response_data
