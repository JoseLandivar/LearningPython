# 1-Definir una función max() que tome como argumento dos números y 
# devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, 
# pero hacerla nosotros mismos es un muy buen ejercicio.

def max(a,b):
    if (a > b):
        print(f'{a} es mayor')
    elif b > a:
        print(f'{b} es mayor')
    else:
        print('Son Iguales')

max(8,4)

# 2-Definir una función max_de_tres(), que tome tres números como argumentos y
# devuelva el mayor de ellos.

def max_de_tres(a,b,c):
    if a > b and a > c:
        print(f'{a} es el mayor')
    elif b > a and b > c:
        print(f'{b} es el mayor')
    elif c > a and c > b:
        print(f'{c} es el mayor')
    else:
        print('Son iguales')

max_de_tres(4,3,3)

# 3-Definir una función que calcule la longitud de una lista o una cadena dada.
# (Es cierto que python tiene la función len() incorporada, 
# pero escribirla por nosotros mismos resulta un muy buen ejercicio.

def largo_cadena (lista):
    cont = 0
    for i in lista:
        cont += 1
    return cont

print(largo_cadena('Hola'))

# 4-Escribir una función que tome un carácter y devuelva True si es una vocal,
# de lo contrario devuelve False.

def caracter(n):
    if n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u':
        return True
    elif n == 'A' or n == 'E' or n == 'I' or n == 'O' or n == 'U':
        return True
    else:
        return False

print(caracter('E'))

# 5- Escribir una función sum() y una función multip() que sumen y multipliquen
# respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4])
# debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def sum (lista):
    suma = 0
    for i in lista:
        suma += i
    return suma

<<<<<<< HEAD
print(sum([1,2,3,4]))

def multip(lista2):
    multi = 1
    for j in lista2:
        multi *= j
    return multi

print(multip([1,2,3,4]))

# 6- Definir una función inversa() que calcule la inversión de una cadena.
# Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def palabra(a):
    print(len(a))

palabra('Hola')
=======
print (sum([1,2,3,4]))

def multi(numbers):
    mult = 1
    for j in numbers:
        mult *= j
    return mult

print(multi([1,2,3,4]))

# 6- Definir una función inversa() que calcule la inversión de una cadena.
# Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def inversa (cadena):
    invertida = ""
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        invertida += cadena[indice]
        indice = indice + (-1)
        cont -= 1
    return invertida

print(inversa('Hola'))

>>>>>>> main
