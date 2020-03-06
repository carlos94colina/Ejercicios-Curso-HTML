import requests

url = "https://openapi.emtmadrid.es/v2/mobilitylabs/user/login/"
headers = {
    "X-ApiKey":   "",
    "X-ClientId": "",
    "passKey":    "",
    }

r = requests.get(url, headers = headers)
token = r.json()["data"][0]["accessToken"]

url = "https://openapi.emtmadrid.es/v1/transport/bicimad/stations/"
headers = {"accessToken": "aaaaefb6-5cc0-11ea-bae2-02dc460b89d8"}

r = requests.get(url, headers = headers)
data = r.json()["data"]

print(f"BiciMad - Estaciones: {len(data)}")
print(f"BiciMad - Bases: {sum(list(map(lambda item: item['total_bases'], data)))}")
print(f"BiciMad - Bicis Alquiladas: {sum(list(map(lambda item: item['free_bases'], data)))}")
print(f"BiciMad - Bicis Ancladas: {sum(list(map(lambda item: item['dock_bikes'], data)))}")
