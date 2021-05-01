#Creando Lista

nombres = ['Jose','Maria','Kathi','Dayana']

#Imprimir la lista nombres
print(nombres)

#Acceder a cada elemento de la lista
print(nombres[0])

print(nombres[3])

#Accediendo de manera inversa
print(nombres[-1])

print(nombres[-4])

#Imprimir por rango 
print(nombres[0:2]) #Sin incluir el indice 2

#Ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ : 3])
#Desde el indice indicado hasta el final
print(nombres[1 : ])

#Cambiar de valor un indice

nombres[3] = 'Marcela'
print(nombres)

#Iterar lista

for nombre in nombres:
    print(nombre)
else:
    print('Fin de la lista')