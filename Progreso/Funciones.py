#Funcion
#Es un bloque de codigo que podemos mandar a llamar
def miFuncion():
    print('Hola desde mi funcion')

miFuncion()
miFuncion()

#Con parametros y argumentos
def miFuncion2(nombre,apellido):
    print('Hola desde mi funcion 2')
    print(f'Hola {nombre} {apellido}')

miFuncion2('Jose','Landivar')
miFuncion2('Sergio','Apuri')

#Suma de dos numero
def suma(a,b):
    return a + b

print(f'El resultado de la suma es: {suma(5,5)}')

resultado = suma(5,3)
print(f'La suma es: {resultado}')

#Valores por default
def suma(a = 0,b = 0) -> int:
    return a + b

print(f'El resultado de la suma es: {suma(2,7)}')

resultado = suma()
print(f'La suma es: {resultado}')

### Argumentos Variables ###

def listarNombres(*args):
    for nombre in args:
        print(nombre)

listarNombres('Jose','Sergio','Juan')
listarNombres('Jessica','Dayana','Ana')

#Crear una función para sumar los valores recibidos de tipo numérico,
#utilizando argumentos variables *args como parámetro de la función y
#regresar como resultado la suma de todos los valores pasados como argumentos.
def sumar_valores(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado


#Crear una función para multiplicar los valores recibidos de tipo numérico,
#utilizando argumentos variables *args como parámetro de la función y
#regresar como resultado la multiplicación de todos los valores pasados como argumentos.
def multiplicar_valores(*args):
    resultado = 0
    for valor in args:
        resultado *= valor
    return resultado

### Diccioneario con Funciones ###
def diccionario(**terminos):
    for llaves, clave in terminos.items():
        print(f'{llaves}:{clave}')

### Listas en funciones ###
def listaNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['Jose','Juan','Sergio']
listaNombres(nombres)
listaNombres('Jose')