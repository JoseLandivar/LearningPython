###    Ciclo For    ###

cadena = 'Hola'

for letra in cadena:
    print(letra)
else:
    print('Fin ciclo For')

#Break

for letras in 'Holanda':
    if letras == 'a':
        print(f'Letra encontrada: {letra}')
        break
else:
    print('Fin')
    
#Continue

for i in range(6):
    if i % 2 == 0:
        print(i)
    
for f in range(6):
    if f % 2 != 0:
        continue
    print(f)    
    
