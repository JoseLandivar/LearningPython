#Funcion que pida e imprima tu nombre
def miFuncion(args):
    nombre = input('Ingrese su nombre: ')
    print(f'Su nombre es {nombre}')
    print('Gracias')
    return nombre

miFuncion('Jose')

#Funcion que pida y sume dos numeros
def funcionSuma():
    num1 = int(input('Ingrese un numero: '))
    num2 = int(input('Ingrese un numero: '))
    suma = num1 + num2
    print(f'La suma es {suma}')

funcionSuma()

#Funcion de pide y multiplique dos numeros
def funcionMulticacion():
    mult1 = int(input('Ingrese un numero: '))
    mult2 = int(input('Ingrese un numero: '))
    multiplicacion = mult1 * mult2
    print(f'La multiplicacion es: {multiplicacion}')

funcionMulticacion()

# Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas.
# Puede ser cualquier valor positivo, ejemplo, si pasamos el valor de 5,
# debe imprimir: 5 4 3 2 1 Si se pasa el valor de 3, debe imprimir: 3 2 1
# Si se pasan valores negativos no imprime nada