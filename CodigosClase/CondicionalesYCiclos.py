# Condicionales

# Sí simple
edad = 25
if edad >= 18:
    print("Eres mayor de edad")

# Sí doble
precio = 501
presupuesto = 500
if precio <= presupuesto:
    print("Si lo compro")
else:
    print("Cuanto es lo mínimo?")

#Sí múltiple
edad = 0
if edad > 60:
    print("Boomer")
elif edad <= 59 and edad >= 45:
    print("Gen X")
elif edad <= 44 and edad >= 35:
    print("Gen Y")
elif edad <= 34 and edad >= 25:
    print("Millenials")
elif edad <= 24 and edad >= 17:
    print("Zentenialls")
elif edad <= 16 and edad >= 8:
    print("Touch babys")
elif edad <= 7 and edad >= 3:
    print("Alpha")
else:
    print("Beta")
   
#Según / switch
edad = 32
match edad:
    case _ if edad > 60:
        print("Boomer")
    case _ if edad in range(45,60):
        print("Gen X")
    case _ if edad <= 44 and edad >= 35:
        print("Gen Y")
    case _ if edad <= 34 and edad >= 25:
        print("Millenials")
    case _ if edad <= 24 and edad >= 17:
        print("Zentenialls")
    case _ if edad <= 16 and edad >= 8:
        print("Touch babys")
    case _ if edad <= 7 and edad >= 3:
        print("Alpha")
    case _ : 
        print("Beta")

# Ciclos

# Hacer-Mientras / Do-While

menu = """
######Ejemplo Menú#####
#                                          #
#        1.- Suma                   #
#        2.- Resta                   #
#        3.- Salir                     #
#                                          #
########################
"""
opcion = int(input(menu+"Ingrese la opción deseada: "))
while opcion < 1 or opcion > 3:
    opcion = int(input(menu+"Ingrese una opción válida: "))    

# Mientras
factorial = 5
acum = 1
while factorial > 0:
    acum *=  factorial
    factorial -= 1
print(acum)

#
int()
float()
str()
# Compuestos
list()
tuple()
set()
#range()
#enumerate()
# Complejo
dict()


# Para
objetoIterable = [1,2,3,4,5,6,7,8,9,0]

for var in objetoIterable:
    print(var)


diccionario = dict()

diccionario["hola"] = 0

for palabra,significado in diccionario.items():
    print(palabra, significado)


# Break
lista = range(10)
for valor in lista:
    print(valor)
    if valor == 7:
        print("proceso se detiene")
        break

#Continue
suma = 0
for valor in range(100):
    if valor % 2 == 0:
        continue
    else:
        print(valor)
        suma += valor
print(suma)

















