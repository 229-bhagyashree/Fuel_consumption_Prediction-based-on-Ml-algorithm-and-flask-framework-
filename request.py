import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'Engine Size':2.4})

print(r.json())