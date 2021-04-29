edad = int(input('Ingrese su edad: '))

dato = None

if (edad >= 0) and (edad <= 10):
    dato = 'La infancia es increible...'
elif (edad >= 11) and (edad <= 20):
    dato = 'Muchos cambios y mucho estudio...'
elif (21 <= edad < 30):
    dato = 'Amor y comienza el trabajo...'
else:
    dato = 'Etapa de la vida no reconocida'
print(f'Tienes {edad} años : {dato}')
    