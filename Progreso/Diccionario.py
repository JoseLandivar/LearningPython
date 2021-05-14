#Esta compuesto por un allave y un valor(Key,Value)

diccionario = {
    'IDE':'Integrated Development Emviroment',
    'OOP':'Object Oriented Programming',
    'DBMS':'DataBase Management System'
}
print(diccionario)

#Conocer el largo
print(len(diccionario))

#Acceder a un elemento(key)
print(diccionario['IDE'])

#Otra Forma de Recuperar un elemento
print(diccionario.get('OOP'))

#Modificar Elementos
diccionario['IDE'] = 'integrated development emviroment'
print(diccionario['IDE'])

#Recorer Elementos
for termino, valor in diccionario.items():
    print(termino, valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

#Comprobar existencia
print('IDE' in diccionario)

#Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

#Remover un elemento
diccionario.pop('DBMS')
print(diccionario)

#Limpiar
diccionario.clear()
print(diccionario)

#Eliminar el diccionario
del diccionario
print(diccionario)