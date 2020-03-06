## Utilizamos el objeto requests para llamar al API
## URL: http://demos.network/api/parking-madrid.ashx
## Method: GET
##
## Key: da0412b0-2038-498a-a809-8a59117775b1
## La Key de acceso se envia como parámetro de la cabecera con el nombre de api-key
##
## Claves del diccionario de Respuesta:
##  - code: distinto de 01, cuando se trata de un error
##  - description: mensaje de error cuando code es distinto de 01
##  - data: contiene el objeto con los datos cuando code es igual a 01
##
## Requerimiento Funcional:
##  - Muestra el número total de parkings de Madrid
##  - Muestra el número total de parkings de la EMT (los objetos de data tiene la propiedad isEmtPark igual a True)
##  - Muestra el número total de parkings de la No EMT (los objetos de data tiene la propiedad isEmtPark igual a False)
##  - Muestra el número total de plazas libres de todos los parkings de Madrid 
##    (la propiedad freeParking contiene el número de plazas libres en tiempo real o None para parkings que no suministran información)
##
##  Utiliza funciones de filtrado o funciones lambda para un código más optimizado
##
##  Puntuación:
##   - Acceso a la información, ser capaz de mostrar la respuesta (3 puntos)
##   - Mostrar los valores solicitados, número de parkings (2 puntos) y plazas libres (2 puntos)
##   - Utilizar funciones de filtrado (2 puntos) o utilizar funciones lambda (3 puntos)
##

import requests

headers = {'api-key': 'da0412b0-2038-498a-a809-8a59117775b1'}
r = requests.get('http://demos.network/api/parking-madrid.ashx', headers = headers)

if(r.json()["code"] == "01"):
    data = r.json()["data"];
    
    print(f"Número de Parking: {len(data)}")
    print(f"Número de Parking EMT: {len(list(filter(lambda x: x['isEmtPark'] == True, data)))}")
    print(f"Número de Parking No EMT: {len(list(filter(lambda x: x['isEmtPark'] != True, data)))}")

    plazas = 0
    for parking in list(filter(lambda x: x['freeParking'] != None, data)):
        plazas += int(parking['freeParking'])

    print(f"Número de Plazas Libres: {plazas}")
else:
    print(f"Error {r.json()['code']}: {r.json()['description']}")

