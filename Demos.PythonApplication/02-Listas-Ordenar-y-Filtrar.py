######################################################################
## Ordenar una lista de números                                     ##
######################################################################
numeros = [ 12, 8, 234, 5, 6 , 78, 234, 98, 11, 4, 23, 76]
numeros.sort()
print(numeros)
numeros.sort(reverse = True)
print(numeros)

######################################################################
## Filtrar o búscar en una lista de números                         ##
######################################################################

## Función de filtrado: número menores de cincuenta
def less50(item):
    if item < 50: return item

print(list(filter(less50, numeros)))

## Función de filtrado: número par
def isEven(item):
    if (item % 2 == 0): return item

print(list(filter(isEven, numeros)))

######################################################################
## Ordenar una lista de valores alfanuméricos                       ##
######################################################################
nombres = ["Carlos", "Jorge", "Javier", "María Ángeles", "Sonia", "Carla"]
nombres.sort()
print(nombres)
nombres.sort(reverse = True)
print(nombres)

## Función de ordenación: número de caracteres
def sort_size(item):
    return len(item)

nombres.sort(key=sort_size)
print(nombres)

## Función de ordenación: alfabéticamente teniendo en cuenta el segunda caracter
def sort_second_char(item):
    return item[1]

nombres.sort(key=sort_second_char)
print(nombres)

## Función de ordenación: alfabéticamente teniendo en cuenta el segundo y último caracter
def sort_special(item):
    return (item[1] + item[len(item) - 1])

nombres.sort(key=sort_special)
print(nombres)

nombres = ["Carlos Sánchez", "Jorge Ramos", "Javier Rozas", "Ángeles Sánchez", "Sonia García", "Carla Rivas"]

## Función de ordenación: alfabéticamente por el apellido
def sort_apellidos(item):
    return item.split(" ")[1]

## Función de ordenación: alfabéticamente por el apellido, cuando el nombre es compuesto
def sort_apellidos2(item):
    return item.split(" ")[len(item.split(" ")) - 1]

nombres.sort(key=sort_apellidos)
print(nombres)

alumnos = ["Carlos Sánchez -Edad: 33", 
           "Jorge Ramos - Edad: 26", 
           "Javier Rozas - Edad: 27", 
           "María Ángeles Sánchez - Edad: 38", 
           "Sonia García - Edad: 22", 
           "Carla Rivas - Edad: 31"]

## Función de ordenación: por la edad
def sort_edad(item):
    return int(item.split(":")[1])

alumnos.sort(key=sort_edad)
print(alumnos)

## Función de Filtrado: busca todos los alumnos con apellido igual a Sánchez
def apellido_Sanchez(item):
	if item.split(" ")[1] == "Sánchez": return item

busqueda = filter(apellido_Sanchez, nombres)
print(list(busqueda))

