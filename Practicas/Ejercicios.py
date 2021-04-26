#Una panadería vende barras de pan a 3.49€ cada una.
#El pan que no es el día tiene un descuento del 60%.
#Escribir un programa que comience leyendo el número de barras vendidas que no son del día.
#Después el programa debe mostrar el precio habitual de una barra de pan,
#el descuento que se le hace por no ser fresca y el coste final total.

barrasDePan = int(input('Ingrese numero de barras de pan que no son del dia vendidas: '))

costoDeLasBarrasDePan = barrasDePan * 3.46
costoConDescuento = costoDeLasBarrasDePan * 0.60
costoFinal = costoDeLasBarrasDePan - costoConDescuento

print(f'El precio total es de: {costoDeLasBarrasDePan}€, con el descuento del 60% es: {costoFinal}€')

#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
#Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete
#así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda.
#Cada payaso pesa 112 g y cada muñeca 75 g.
#Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido
#y calcule el peso total del paquete que será enviado.

payasos = int(input('Ingrese numero de payasos vendidos: '))
muñecas = int(input('Ingrese numero de muñecas vendidas: '))

precioPayasos = payasos * 0.112
precioMuñecas = muñecas * 0.075
pesoTotal = precioPayasos + precioMuñecas

print(f'El peso de los payason vendidos es de: {precioPayasos}Kg. y el de las muñecas es de {precioMuñecas}Kg., El peso total del paquete sera de {pesoTotal}Kg')
