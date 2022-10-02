import requests
response = requests.get("https://api.n2yo.com/rest/v1/satellite/positions/31135/41.702/-76.014/0/2/&apiKey=DN7JCW-RE8XWM-FJM3S9-4XO8")

agile = response.json()

lat = agile['positions'][0]['satlatitude']
long = agile['positions'][0]['satlongitude']

print(lat, long)