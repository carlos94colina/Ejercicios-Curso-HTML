import sqlite3
from pymongo import MongoClient
from pymongo.collation import Collation
from bson.objectid import ObjectId

## Establece conexión con mongoDB
mongo = MongoClient('mongodb://localhost:27017/')

## Conexión con la Base de Datos
conn = sqlite3.connect('productos.db')
cursor = conn.cursor()

## Comprobación de que la tabla productos no existe
cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='productos';")
r = cursor.fetchone()

if(int(r[0]) == 0): 
    cursor.execute("CREATE TABLE productos (ProductID, ProductName, UnitPrice, UnitsInStock)")

###########################################################

datos = list(mongo.northwind.products.find({}, {"ProductID": 1, "ProductName": 1, "UnitPrice": 1, "UnitsInStock": 1, "_id": 0}))
cursor.executemany('INSERT INTO productos VALUES (:ProductID,:ProductName,:UnitPrice,:UnitsInStock)', datos)
conn.commit()

print("Importación Finalizada")


