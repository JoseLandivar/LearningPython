#Iterar un rango de 0 a 10 e imprimir números divisibles entre 3

lista = [0,1,2,3,4,5,6,7,8,9,10]
print(lista)

for n in lista:
    if n % 3 == 0:
        print(n)
        
#Dada la siguiente tupla, crear una lista que sólo incluya los números menor que 5
#utilizando un ciclo for: tupla = (13, 1, 8, 3, 2, 5, 8)

tupla = (13,1,8,3,2,5,8)
lista = list(tupla)

for lista in tupla:
    if lista <= 5:
        print(lista)