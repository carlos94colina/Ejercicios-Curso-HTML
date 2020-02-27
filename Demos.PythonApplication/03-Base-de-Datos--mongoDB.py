import json
from pymongo import MongoClient
from pymongo.collation import Collation
from bson.objectid import ObjectId

from pprint import pprint

## Establece conexión con la base de datos
client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017/')

## Ejecutar un comando
resultado = client.admin.command("serverStatus")
print(f"Conexiones disponibles: {resultado['connections']['available']}")

## Extraer información de un documento
print(resultado['process'])
path = resultado['process'].split('\\')
print(path)

path.pop(len(path) - 1)
print(path)

path = '\\'.join(path) + '\\'
print(f"La ruta de instalación es: {path}")

## Buscar documentos: clientes de USA
for item in client.northwind.customers.find({ "Country" : "USA" }):
    print(f"{item['CustomerID']}# {item['CompanyName']} - {item['Country']}")

## Contar documentos: clientes de USA
numero = client.northwind.customers.count_documents({ "Country" : "USA" })
print(f"{numero} registros encontrados")
