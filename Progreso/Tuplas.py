
#Tuplas es paracido a las listas pero no se puede agregar ni modoficar(inmutable)

#Definir Tupla
frutas = ('Naranja','Manzana','Guayaba')
print(frutas)

#Largo de la Tupla
print(len(frutas))

#Acceder a un elemento
print(frutas[1])

#Navegacion Inversa
print(frutas[-1])

#Acceder a u rango
print(frutas[0:2])

#Recorrer elementos
for varFrutas in frutas:
    print(varFrutas, end=' ')
    print(end='\n')
    
#Convertir tupla en lista
frutaLista = list(frutas)
print(frutaLista)

#Convertir de lista a tupla
frutaTupla = tuple(frutaLista)
print(frutaTupla)

#ELiminar la tupla
del frutaTupla
print(frutaTupla)

### Set en Python ###
#Notiene indices, no se puede modificar, ni duplicados

planetas = {'Marte','Jupiter','Venus'}
print(planetas)

#Ver el largo
print(len(planetas))

#Buscar un elemento
print('Marte' in planetas)

#Agregar elemento
planetas.add('Tierra')
print(planetas)

#Eliminar elementos
planetas.remove('Venus')
print(planetas)

#Limpiar Set
planetas.clear()
print(planetas)

#Eliminar todo el set
del planetas
print(planetas)