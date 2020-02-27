######################################################################
## Trabajar la ordenación y filtrado de colecciones                 ##
######################################################################
import json

datos = """[
{"ProductID":"1","ProductName":"Chai","SupplierID":"1","CategoryID":"1","QuantityPerUnit":"10 boxes x 20 bags","UnitPrice":"18.00","UnitsInStock":"39","UnitsOnOrder":"0","ReorderLevel":"10","Discontinued":"0"},
{"ProductID":"2","ProductName":"Chang","SupplierID":"1","CategoryID":"1","QuantityPerUnit":"24 - 12 oz bottles","UnitPrice":"19.00","UnitsInStock":"17","UnitsOnOrder":"40","ReorderLevel":"25","Discontinued":"0"},
{"ProductID":"3","ProductName":"Aniseed Syrup","SupplierID":"1","CategoryID":"2","QuantityPerUnit":"12 - 550 ml bottles","UnitPrice":"10.00","UnitsInStock":"13","UnitsOnOrder":"70","ReorderLevel":"25","Discontinued":"0"},
{"ProductID":"4","ProductName":"Chef Anton's Cajun Seasoning","SupplierID":"2","CategoryID":"2","QuantityPerUnit":"48 - 6 oz jars","UnitPrice":"22.00","UnitsInStock":"53","UnitsOnOrder":"0","ReorderLevel":"0","Discontinued":"0"},
{"ProductID":"5","ProductName":"Chef Anton's Gumbo Mix","SupplierID":"2","CategoryID":"2","QuantityPerUnit":"36 boxes","UnitPrice":"21.35","UnitsInStock":"0","UnitsOnOrder":"0","ReorderLevel":"0","Discontinued":"1"},
{"ProductID":"6","ProductName":"Grandma's Boysenberry Spread","SupplierID":"3","CategoryID":"2","QuantityPerUnit":"12 - 8 oz jars","UnitPrice":"25.00","UnitsInStock":"120","UnitsOnOrder":"0","ReorderLevel":"25","Discontinued":"0"},
{"ProductID":"7","ProductName":"Uncle Bob's Organic Dried Pears","SupplierID":"3","CategoryID":"7","QuantityPerUnit":"12 - 1 lb pkgs.","UnitPrice":"30.00","UnitsInStock":"15","UnitsOnOrder":"0","ReorderLevel":"10","Discontinued":"0"},
{"ProductID":"8","ProductName":"Northwoods Cranberry Sauce","SupplierID":"3","CategoryID":"2","QuantityPerUnit":"12 - 12 oz jars","UnitPrice":"40.00","UnitsInStock":"6","UnitsOnOrder":"0","ReorderLevel":"0","Discontinued":"0"},
{"ProductID":"9","ProductName":"Mishi Kobe Niku","SupplierID":"4","CategoryID":"6","QuantityPerUnit":"18 - 500 g pkgs.","UnitPrice":"97.00","UnitsInStock":"29","UnitsOnOrder":"0","ReorderLevel":"0","Discontinued":"1"},
{"ProductID":"10","ProductName":"Ikura","SupplierID":"4","CategoryID":"8","QuantityPerUnit":"12 - 200 ml jars","UnitPrice":"31.00","UnitsInStock":"31","UnitsOnOrder":"0","ReorderLevel":"0","Discontinued":"0"},
{"ProductID":"11","ProductName":"Queso Cabrales","SupplierID":"5","CategoryID":"4","QuantityPerUnit":"1 kg pkg.","UnitPrice":"21.00","UnitsInStock":"22","UnitsOnOrder":"30","ReorderLevel":"30","Discontinued":"0"},
{"ProductID":"12","ProductName":"Queso Manchego La Pastora","SupplierID":"5","CategoryID":"4","QuantityPerUnit":"10 - 500 g pkgs.","UnitPrice":"38.00","UnitsInStock":"86","UnitsOnOrder":"0","ReorderLevel":"0","Discontinued":"0"},
{"ProductID":"13","ProductName":"Konbu","SupplierID":"6","CategoryID":"8","QuantityPerUnit":"2 kg box","UnitPrice":"6.00","UnitsInStock":"24","UnitsOnOrder":"0","ReorderLevel":"5","Discontinued":"0"},
{"ProductID":"14","ProductName":"Tofu","SupplierID":"6","CategoryID":"7","QuantityPerUnit":"40 - 100 g pkgs.","UnitPrice":"23.25","UnitsInStock":"35","UnitsOnOrder":"0","ReorderLevel":"0","Discontinued":"0"},
{"ProductID":"15","ProductName":"Genen Shouyu","SupplierID":"6","CategoryID":"2","QuantityPerUnit":"24 - 250 ml bottles","UnitPrice":"15.50","UnitsInStock":"39","UnitsOnOrder":"0","ReorderLevel":"5","Discontinued":"0"},
{"ProductID":"16","ProductName":"Pavlova","SupplierID":"7","CategoryID":"3","QuantityPerUnit":"32 - 500 g boxes","UnitPrice":"17.45","UnitsInStock":"29","UnitsOnOrder":"0","ReorderLevel":"10","Discontinued":"0"},
{"ProductID":"17","ProductName":"Alice Mutton","SupplierID":"7","CategoryID":"6","QuantityPerUnit":"20 - 1 kg tins","UnitPrice":"39.00","UnitsInStock":"0","UnitsOnOrder":"0","ReorderLevel":"0","Discontinued":"1"},
{"ProductID":"18","ProductName":"Carnarvon Tigers","SupplierID":"7","CategoryID":"8","QuantityPerUnit":"16 kg pkg.","UnitPrice":"62.50","UnitsInStock":"42","UnitsOnOrder":"0","ReorderLevel":"0","Discontinued":"0"},
{"ProductID":"19","ProductName":"Teatime Chocolate Biscuits","SupplierID":"8","CategoryID":"3","QuantityPerUnit":"10 boxes x 12 pieces","UnitPrice":"9.20","UnitsInStock":"25","UnitsOnOrder":"0","ReorderLevel":"5","Discontinued":"0"},
{"ProductID":"20","ProductName":"Sir Rodney's Marmalade","SupplierID":"8","CategoryID":"3","QuantityPerUnit":"30 gift boxes","UnitPrice":"81.00","UnitsInStock":"40","UnitsOnOrder":"0","ReorderLevel":"0","Discontinued":"0"},
{"ProductID":"21","ProductName":"Sir Rodney's Scones","SupplierID":"8","CategoryID":"3","QuantityPerUnit":"24 pkgs. x 4 pieces","UnitPrice":"10.00","UnitsInStock":"3","UnitsOnOrder":"40","ReorderLevel":"5","Discontinued":"0"},
{"ProductID":"22","ProductName":"Gustaf's Knäckebröd","SupplierID":"9","CategoryID":"5","QuantityPerUnit":"24 - 500 g pkgs.","UnitPrice":"21.00","UnitsInStock":"104","UnitsOnOrder":"0","ReorderLevel":"25","Discontinued":"0"},
{"ProductID":"23","ProductName":"Tunnbröd","SupplierID":"9","CategoryID":"5","QuantityPerUnit":"12 - 250 g pkgs.","UnitPrice":"9.00","UnitsInStock":"61","UnitsOnOrder":"0","ReorderLevel":"25","Discontinued":"0"},
{"ProductID":"24","ProductName":"Guaraná Fantástica","SupplierID":"10","CategoryID":"1","QuantityPerUnit":"12 - 355 ml cans","UnitPrice":"4.50","UnitsInStock":"20","UnitsOnOrder":"0","ReorderLevel":"0","Discontinued":"1"},
{"ProductID":"25","ProductName":"NuNuCa Nuß-Nougat-Creme","SupplierID":"11","CategoryID":"3","QuantityPerUnit":"20 - 450 g glasses","UnitPrice":"14.00","UnitsInStock":"76","UnitsOnOrder":"0","ReorderLevel":"30","Discontinued":"0"},
{"ProductID":"26","ProductName":"Gumbär Gummibärchen","SupplierID":"11","CategoryID":"3","QuantityPerUnit":"100 - 250 g bags","UnitPrice":"31.23","UnitsInStock":"15","UnitsOnOrder":"0","ReorderLevel":"0","Discontinued":"0"},
{"ProductID":"27","ProductName":"Schoggi Schokolade","SupplierID":"11","CategoryID":"3","QuantityPerUnit":"100 - 100 g pieces","UnitPrice":"43.90","UnitsInStock":"49","UnitsOnOrder":"0","ReorderLevel":"30","Discontinued":"0"},
{"ProductID":"28","ProductName":"Rössle Sauerkraut","SupplierID":"12","CategoryID":"7","QuantityPerUnit":"25 - 825 g cans","UnitPrice":"45.60","UnitsInStock":"26","UnitsOnOrder":"0","ReorderLevel":"0","Discontinued":"1"},
{"ProductID":"29","ProductName":"Thüringer Rostbratwurst","SupplierID":"12","CategoryID":"6","QuantityPerUnit":"50 bags x 30 sausgs.","UnitPrice":"123.79","UnitsInStock":"0","UnitsOnOrder":"0","ReorderLevel":"0","Discontinued":"1"},
{"ProductID":"30","ProductName":"Nord-Ost Matjeshering","SupplierID":"13","CategoryID":"8","QuantityPerUnit":"10 - 200 g glasses","UnitPrice":"25.89","UnitsInStock":"10","UnitsOnOrder":"0","ReorderLevel":"15","Discontinued":"0"},
{"ProductID":"31","ProductName":"Gorgonzola Telino","SupplierID":"14","CategoryID":"4","QuantityPerUnit":"12 - 100 g pkgs","UnitPrice":"12.50","UnitsInStock":"0","UnitsOnOrder":"70","ReorderLevel":"20","Discontinued":"0"},
{"ProductID":"32","ProductName":"Mascarpone Fabioli","SupplierID":"14","CategoryID":"4","QuantityPerUnit":"24 - 200 g pkgs.","UnitPrice":"32.00","UnitsInStock":"9","UnitsOnOrder":"40","ReorderLevel":"25","Discontinued":"0"},
{"ProductID":"33","ProductName":"Geitost","SupplierID":"15","CategoryID":"4","QuantityPerUnit":"500 g","UnitPrice":"2.50","UnitsInStock":"112","UnitsOnOrder":"0","ReorderLevel":"20","Discontinued":"0"},
{"ProductID":"34","ProductName":"Sasquatch Ale","SupplierID":"16","CategoryID":"1","QuantityPerUnit":"24 - 12 oz bottles","UnitPrice":"14.00","UnitsInStock":"111","UnitsOnOrder":"0","ReorderLevel":"15","Discontinued":"0"},
{"ProductID":"35","ProductName":"Steeleye Stout","SupplierID":"16","CategoryID":"1","QuantityPerUnit":"24 - 12 oz bottles","UnitPrice":"18.00","UnitsInStock":"20","UnitsOnOrder":"0","ReorderLevel":"15","Discontinued":"0"},
{"ProductID":"36","ProductName":"Inlagd Sill","SupplierID":"17","CategoryID":"8","QuantityPerUnit":"24 - 250 g  jars","UnitPrice":"19.00","UnitsInStock":"112","UnitsOnOrder":"0","ReorderLevel":"20","Discontinued":"0"},
{"ProductID":"37","ProductName":"Gravad lax","SupplierID":"17","CategoryID":"8","QuantityPerUnit":"12 - 500 g pkgs.","UnitPrice":"26.00","UnitsInStock":"11","UnitsOnOrder":"50","ReorderLevel":"25","Discontinued":"0"},
{"ProductID":"38","ProductName":"Côte de Blaye","SupplierID":"18","CategoryID":"1","QuantityPerUnit":"12 - 75 cl bottles","UnitPrice":"263.50","UnitsInStock":"17","UnitsOnOrder":"0","ReorderLevel":"15","Discontinued":"0"},
{"ProductID":"39","ProductName":"Chartreuse verte","SupplierID":"18","CategoryID":"1","QuantityPerUnit":"750 cc per bottle","UnitPrice":"18.00","UnitsInStock":"69","UnitsOnOrder":"0","ReorderLevel":"5","Discontinued":"0"},
{"ProductID":"40","ProductName":"Boston Crab Meat","SupplierID":"19","CategoryID":"8","QuantityPerUnit":"24 - 4 oz tins","UnitPrice":"18.40","UnitsInStock":"123","UnitsOnOrder":"0","ReorderLevel":"30","Discontinued":"0"},
{"ProductID":"41","ProductName":"Jack's New England Clam Chowder","SupplierID":"19","CategoryID":"8","QuantityPerUnit":"12 - 12 oz cans","UnitPrice":"9.65","UnitsInStock":"85","UnitsOnOrder":"0","ReorderLevel":"10","Discontinued":"0"},
{"ProductID":"42","ProductName":"Singaporean Hokkien Fried Mee","SupplierID":"20","CategoryID":"5","QuantityPerUnit":"32 - 1 kg pkgs.","UnitPrice":"14.00","UnitsInStock":"26","UnitsOnOrder":"0","ReorderLevel":"0","Discontinued":"1"},
{"ProductID":"43","ProductName":"Ipoh Coffee","SupplierID":"20","CategoryID":"1","QuantityPerUnit":"16 - 500 g tins","UnitPrice":"46.00","UnitsInStock":"17","UnitsOnOrder":"10","ReorderLevel":"25","Discontinued":"0"},
{"ProductID":"44","ProductName":"Gula Malacca","SupplierID":"20","CategoryID":"2","QuantityPerUnit":"20 - 2 kg bags","UnitPrice":"19.45","UnitsInStock":"27","UnitsOnOrder":"0","ReorderLevel":"15","Discontinued":"0"},
{"ProductID":"45","ProductName":"Rogede sild","SupplierID":"21","CategoryID":"8","QuantityPerUnit":"1k pkg.","UnitPrice":"9.50","UnitsInStock":"5","UnitsOnOrder":"70","ReorderLevel":"15","Discontinued":"0"},
{"ProductID":"46","ProductName":"Spegesild","SupplierID":"21","CategoryID":"8","QuantityPerUnit":"4 - 450 g glasses","UnitPrice":"12.00","UnitsInStock":"95","UnitsOnOrder":"0","ReorderLevel":"0","Discontinued":"0"},
{"ProductID":"47","ProductName":"Zaanse koeken","SupplierID":"22","CategoryID":"3","QuantityPerUnit":"10 - 4 oz boxes","UnitPrice":"9.50","UnitsInStock":"36","UnitsOnOrder":"0","ReorderLevel":"0","Discontinued":"0"},
{"ProductID":"48","ProductName":"Chocolade","SupplierID":"22","CategoryID":"3","QuantityPerUnit":"10 pkgs.","UnitPrice":"12.75","UnitsInStock":"15","UnitsOnOrder":"70","ReorderLevel":"25","Discontinued":"0"},
{"ProductID":"49","ProductName":"Maxilaku","SupplierID":"23","CategoryID":"3","QuantityPerUnit":"24 - 50 g pkgs.","UnitPrice":"20.00","UnitsInStock":"10","UnitsOnOrder":"60","ReorderLevel":"15","Discontinued":"0"},
{"ProductID":"50","ProductName":"Valkoinen suklaa","SupplierID":"23","CategoryID":"3","QuantityPerUnit":"12 - 100 g bars","UnitPrice":"16.25","UnitsInStock":"65","UnitsOnOrder":"0","ReorderLevel":"30","Discontinued":"0"},
{"ProductID":"51","ProductName":"Manjimup Dried Apples","SupplierID":"24","CategoryID":"7","QuantityPerUnit":"50 - 300 g pkgs.","UnitPrice":"53.00","UnitsInStock":"20","UnitsOnOrder":"0","ReorderLevel":"10","Discontinued":"0"},
{"ProductID":"52","ProductName":"Filo Mix","SupplierID":"24","CategoryID":"5","QuantityPerUnit":"16 - 2 kg boxes","UnitPrice":"7.00","UnitsInStock":"38","UnitsOnOrder":"0","ReorderLevel":"25","Discontinued":"0"},
{"ProductID":"53","ProductName":"Perth Pasties","SupplierID":"24","CategoryID":"6","QuantityPerUnit":"48 pieces","UnitPrice":"32.80","UnitsInStock":"0","UnitsOnOrder":"0","ReorderLevel":"0","Discontinued":"1"},
{"ProductID":"54","ProductName":"Tourtière","SupplierID":"25","CategoryID":"6","QuantityPerUnit":"16 pies","UnitPrice":"7.45","UnitsInStock":"21","UnitsOnOrder":"0","ReorderLevel":"10","Discontinued":"0"},
{"ProductID":"55","ProductName":"Pâté chinois","SupplierID":"25","CategoryID":"6","QuantityPerUnit":"24 boxes x 2 pies","UnitPrice":"24.00","UnitsInStock":"115","UnitsOnOrder":"0","ReorderLevel":"20","Discontinued":"0"},
{"ProductID":"56","ProductName":"Gnocchi di nonna Alice","SupplierID":"26","CategoryID":"5","QuantityPerUnit":"24 - 250 g pkgs.","UnitPrice":"38.00","UnitsInStock":"21","UnitsOnOrder":"10","ReorderLevel":"30","Discontinued":"0"},
{"ProductID":"57","ProductName":"Ravioli Angelo","SupplierID":"26","CategoryID":"5","QuantityPerUnit":"24 - 250 g pkgs.","UnitPrice":"19.50","UnitsInStock":"36","UnitsOnOrder":"0","ReorderLevel":"20","Discontinued":"0"},
{"ProductID":"58","ProductName":"Escargots de Bourgogne","SupplierID":"27","CategoryID":"8","QuantityPerUnit":"24 pieces","UnitPrice":"13.25","UnitsInStock":"62","UnitsOnOrder":"0","ReorderLevel":"20","Discontinued":"0"},
{"ProductID":"59","ProductName":"Raclette Courdavault","SupplierID":"28","CategoryID":"4","QuantityPerUnit":"5 kg pkg.","UnitPrice":"55.00","UnitsInStock":"79","UnitsOnOrder":"0","ReorderLevel":"0","Discontinued":"0"},
{"ProductID":"60","ProductName":"Camembert Pierrot","SupplierID":"28","CategoryID":"4","QuantityPerUnit":"15 - 300 g rounds","UnitPrice":"34.00","UnitsInStock":"19","UnitsOnOrder":"0","ReorderLevel":"0","Discontinued":"0"},
{"ProductID":"61","ProductName":"Sirop d'érable","SupplierID":"29","CategoryID":"2","QuantityPerUnit":"24 - 500 ml bottles","UnitPrice":"28.50","UnitsInStock":"113","UnitsOnOrder":"0","ReorderLevel":"25","Discontinued":"0"},
{"ProductID":"62","ProductName":"Tarte au sucre","SupplierID":"29","CategoryID":"3","QuantityPerUnit":"48 pies","UnitPrice":"49.30","UnitsInStock":"17","UnitsOnOrder":"0","ReorderLevel":"0","Discontinued":"0"},
{"ProductID":"63","ProductName":"Vegie-spread","SupplierID":"7","CategoryID":"2","QuantityPerUnit":"15 - 625 g jars","UnitPrice":"43.90","UnitsInStock":"24","UnitsOnOrder":"0","ReorderLevel":"5","Discontinued":"0"},
{"ProductID":"64","ProductName":"Wimmers gute Semmelknödel","SupplierID":"12","CategoryID":"5","QuantityPerUnit":"20 bags x 4 pieces","UnitPrice":"33.25","UnitsInStock":"22","UnitsOnOrder":"80","ReorderLevel":"30","Discontinued":"0"},
{"ProductID":"65","ProductName":"Louisiana Fiery Hot Pepper Sauce","SupplierID":"2","CategoryID":"2","QuantityPerUnit":"32 - 8 oz bottles","UnitPrice":"21.05","UnitsInStock":"76","UnitsOnOrder":"0","ReorderLevel":"0","Discontinued":"0"},
{"ProductID":"66","ProductName":"Louisiana Hot Spiced Okra","SupplierID":"2","CategoryID":"2","QuantityPerUnit":"24 - 8 oz jars","UnitPrice":"17.00","UnitsInStock":"4","UnitsOnOrder":"100","ReorderLevel":"20","Discontinued":"0"},
{"ProductID":"67","ProductName":"Laughing Lumberjack Lager","SupplierID":"16","CategoryID":"1","QuantityPerUnit":"24 - 12 oz bottles","UnitPrice":"14.00","UnitsInStock":"52","UnitsOnOrder":"0","ReorderLevel":"10","Discontinued":"0"},
{"ProductID":"68","ProductName":"Scottish Longbreads","SupplierID":"8","CategoryID":"3","QuantityPerUnit":"10 boxes x 8 pieces","UnitPrice":"12.50","UnitsInStock":"6","UnitsOnOrder":"10","ReorderLevel":"15","Discontinued":"0"},
{"ProductID":"69","ProductName":"Gudbrandsdalsost","SupplierID":"15","CategoryID":"4","QuantityPerUnit":"10 kg pkg.","UnitPrice":"36.00","UnitsInStock":"26","UnitsOnOrder":"0","ReorderLevel":"15","Discontinued":"0"},
{"ProductID":"70","ProductName":"Outback Lager","SupplierID":"7","CategoryID":"1","QuantityPerUnit":"24 - 355 ml bottles","UnitPrice":"15.00","UnitsInStock":"15","UnitsOnOrder":"10","ReorderLevel":"30","Discontinued":"0"},
{"ProductID":"71","ProductName":"Flotemysost","SupplierID":"15","CategoryID":"4","QuantityPerUnit":"10 - 500 g pkgs.","UnitPrice":"21.50","UnitsInStock":"26","UnitsOnOrder":"0","ReorderLevel":"0","Discontinued":"0"},
{"ProductID":"72","ProductName":"Mozzarella di Giovanni","SupplierID":"14","CategoryID":"4","QuantityPerUnit":"24 - 200 g pkgs.","UnitPrice":"34.80","UnitsInStock":"14","UnitsOnOrder":"0","ReorderLevel":"0","Discontinued":"0"},
{"ProductID":"73","ProductName":"Röd Kaviar","SupplierID":"17","CategoryID":"8","QuantityPerUnit":"24 - 150 g jars","UnitPrice":"15.00","UnitsInStock":"101","UnitsOnOrder":"0","ReorderLevel":"5","Discontinued":"0"},
{"ProductID":"74","ProductName":"Longlife Tofu","SupplierID":"4","CategoryID":"7","QuantityPerUnit":"5 kg pkg.","UnitPrice":"10.00","UnitsInStock":"4","UnitsOnOrder":"20","ReorderLevel":"5","Discontinued":"0"},
{"ProductID":"75","ProductName":"Rhönbräu Klosterbier","SupplierID":"12","CategoryID":"1","QuantityPerUnit":"24 - 0.5 l bottles","UnitPrice":"7.75","UnitsInStock":"125","UnitsOnOrder":"0","ReorderLevel":"25","Discontinued":"0"},
{"ProductID":"76","ProductName":"Lakkalikööri","SupplierID":"23","CategoryID":"1","QuantityPerUnit":"500 ml","UnitPrice":"18.00","UnitsInStock":"57","UnitsOnOrder":"0","ReorderLevel":"20","Discontinued":"0"},
{"ProductID":"77","ProductName":"Original Frankfurter grüne Soße","SupplierID":"12","CategoryID":"2","QuantityPerUnit":"12 boxes","UnitPrice":"13.00","UnitsInStock":"32","UnitsOnOrder":"0","ReorderLevel":"15","Discontinued":"0"}
]"""

productos = json.loads(datos)

## Buscar productos con un precio superior a 100
def priceGreater100(item):
    if (float(item['UnitPrice']) > 100): 
        return True
busqueda = list(filter(priceGreater100, productos))

## Buscar productos con un precio superior a 100, con lambda
busqueda2 = list(filter(lambda item: float(item['UnitPrice']) > 100 ,productos))
print(f"Existen {len(busqueda)} productos con precio mayor de 100")

## Buscar productos con un precio inferior a 100 y stock superior a 5
def stockAndPrice(item):
    if (float(item['UnitPrice']) < 100) & (int(item['UnitsInStock']) > 5): 
        return True
busqueda = list(filter(stockAndPrice, productos))

## Buscar productos con un precio inferior a 100 y stock superior a 5, con lambda
busqueda2 = list(filter(lambda x: (float(x['UnitPrice']) < 100) & (int(x['UnitsInStock']) > 5) ,productos))

print(f"{len(busqueda)} productos con precio inferior a 50 y más de 5 unidades")

## Buscar productos que contengan en su nombre de producto la palabra Queso
def nameQueso(item):
    if("Queso" in item['ProductName']):
        return True    
busqueda = list(filter(nameQueso, productos))

## Buscar productos que contengan en su nombre de producto la palabra Queso, con lambda
busqueda2 = list(filter(lambda x: "Queso" in x['ProductName'], productos))

for producto in busqueda:
    print(f"{producto['ProductID']}# {producto['ProductName']} - {producto['UnitPrice']}")



