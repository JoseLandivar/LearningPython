print('Proprocione los datos del libro:')
nombre = input('Ingrese nombre del libro: ')
id = int(input('Ingrese Id del libro: '))
precio = float(input('Ingrese precio del libro: '))
envio = input('Indica si el envio es gratuito(True/False): ')

if envio:
    print('Si')
else:
    print('No')
    

print(f'''
Nombre: {nombre}
Id: {id}
Presio: {precio}
      ''')
if envio == 'True':
    print('Envio gratuito?: Si')
else:
    print('Envio gratuito?: No')