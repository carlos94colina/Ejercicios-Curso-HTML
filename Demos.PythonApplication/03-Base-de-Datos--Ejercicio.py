######################################################################
## Mostrar el total de cada pedido de un cliente                    ##
## Mostrar la suma total de todos los pedidos un cliente            ##
######################################################################
import json
from pymongo import MongoClient
from pymongo.collation import Collation
from bson.objectid import ObjectId
from os import system, name 
  
clienteid = ""

## Conexión mongoDB
db = MongoClient('mongodb://localhost:27017/')

while(clienteid != "fin"):
    ## Preguntamos el ID del Cliente
    print("ID Cliente o fin:")
    clienteid = input()
    _ = system("cls")

    if (clienteid != "fin"):
        ## Buscar al cliente en la base de datos mediante el ID
        cliente = db.northwind.customers.find_one({ "CustomerID" : clienteid })
        
        if (cliente == None):   # El cliente no existe
            print(f"No existe un cliente con identificador {clienteid}.")
        else:                   # El cliente existe
            # Buscar el número de pedidos del cliente en la base de datos
            numPedidos = db.northwind.oders.count_documents({ "CustomerID" : clienteid })
            # Buscar información de los pedidos del cliente en la base de datos
            pedidos = db.northwind.oders.find({ "CustomerID" : clienteid })

            if (numPedidos == 0):   # No hay pedidos
                print(f"No hay pedidos registrados para {cliente['CompanyName']}")
            else:                   # Hay pedidos
                totalgeneral = 0
                print(f"Facturación de {cliente['CompanyName']}")
                print("=============================================================================")
                # Recorremos la colección de los pedidos encontrados del cliente
                for item in pedidos:
                    totalpedido = 0
                    # Recorremos el detalle de cada pedido para calcular el total, precio x cantidad
                    for linea in db.northwind.order_details.find({ "OrderID" : item['OrderID'] }):
                        totalpedido += (float(linea['UnitPrice']) * float(linea['Quantity']))
                    
                    # Pintamos el total del pedido
                    print(f"Pedios: {item['OrderID']:<12} --> " + f"{totalpedido:1.2f}".rjust(10, ' '))
                    # Sumamos el total del pedido al total general del cliente
                    totalgeneral += totalpedido

                # Pintamos el total general del cliente
                print("=============================================================================")
                print(f"Facturación Total    --> " + f"{totalgeneral:1.2f}".rjust(10, ' '))
                print("=============================================================================")

print("Fin del Programa")

