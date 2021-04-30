operandoA = 3
operandoB = 2

suma = operandoA + operandoB

#print('Resultado Suma: ',suma)

#Interpolacion
print(f'Resultado suma: {suma} ')

resta = operandoA - operandoB

print(f'Resultado resta: {resta} ')

multiplicacion = operandoA * operandoB

print(f'Resultado multiplicacion: {multiplicacion} ')

division = operandoA / operandoB

print(f'Resultado division: {division} ')

division = operandoA // operandoB

print(f'Resultado division:(int) {division} ')

modulo = operandoA % operandoB

print(f'Resultado modulo: {modulo} ')

exponente = operandoA ** operandoB

print(f'Resultado exponente: {exponente} ')

#Operadores de Asignacion

#Variable = 10
miVariable = 10
print(miVariable)

#Variable + 10 = 11
miVariable += 1
print(miVariable)

#Variable - 1 = 10
miVariable -= 1
print(miVariable)

#Variable * 3 = 30
miVariable *= 3
print(miVariable)

#Variable / 2 = 15
miVariable /= 2
print(miVariable)


#Variables de Comparacion

a = 4
b = 2

result = a == b
print(f'Resultado ==:{result}')

result = a != b
print(f'Resultado !=:{result}')

result = a > b
print(f'Resultado >:{result}')

result = a < b
print(f'Resultado <:{result}')


######Operadores Logicos#######

a = True
b = True
resultado = a and b
print(resultado)

resultado = a or b
print(resultado)

resultado = not a
print(resultado)

##ejemplo##

num = int(input('Ingrese un numero: '))
rangomin = 0
rangomax = 5

dentroderango = (num >= rangomin) and (num <= rangomax)

print(dentroderango)