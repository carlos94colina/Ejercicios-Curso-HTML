import requests
import json

url = "https://openapi.emtmadrid.es/v2/mobilitylabs/user/login/"
headers = {
    "X-ApiKey":   "",
    "X-ClientId": "",
    "passKey":    "",
    }

r = requests.get(url, headers = headers)
token = r.json()["data"][0]["accessToken"]

print("Número de Parada:")
parada = input()

url = "https://openapi.emtmadrid.es/v2/transport/busemtmad/stops/" + parada + "/arrives/"
headers = {"accessToken": "aaaaefb6-5cc0-11ea-bae2-02dc460b89d8"}
datos = {"cultureInfo":"ES", "Text_StopRequired_YN":"Y", "Text_EstimationsRequired_YN":"Y", "Text_IncidencesRequired_YN":"N", "DateTime_Referenced_Incidencies_YYYYMMDD":"20200303"}

r = requests.post(url, headers = headers, data = json.dumps(datos))
data = r.json()["data"][0]["Arrive"]
parada = r.json()["data"][0]["StopInfo"][0]

print(f"Parada: {parada['stopId']} - {parada['stopName']}")
print(f"===========================================================")

for item in data:
    print(f"{item['line']} a {item['DistanceBus'] / 1000} metros ({item['estimateArrive'] // 60} min.)")

print(f"===========================================================")
