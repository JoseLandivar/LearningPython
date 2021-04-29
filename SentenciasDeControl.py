###   If/Else   ###

condicion = 'Hola'

if condicion == True:
    print('Condicion Verdadera')
elif condicion == False:
    print('Condicion Falsa')
else:
    print('Condicion no reconocida')
    
###    Conversion de numero a texto   ###

numero = int(input("Ingrese un numero del 1 al 3: "))
numeroTexto = ''

    if numero == 1:
        numeroTexto = 'Numero Uno'
    elif numero == 2:
        numeroTexto = 'Numero Dos'
    elif numero == 3:
        numeroTexto = 'Numero Tres'
    else:
        numeroTexto = 'Numero Fuera de Rango'
    
print(f'El numero es: {numeroTexto}')

###    Version simplificada de If/Else    ###

print('Condicion verdadera') if condicion else print('Condicion falsa')
    
    
    
    
    