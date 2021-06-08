class Persona:
    def __init__(self):
        self.nombre = 'Jose'
        self.apellido = 'Landivar'
        self.edad = 25

persona1 = Persona()

print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

##Self=this##

class Persona:
    def __init__(self, nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrarDetalle(self):
        print(f'Persona 4: {self.nombre} {self.apellido} {self.edad}')
        pass

persona2 = Persona('Juan','Landivar',9)
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)

persona3 = Persona('Sergio','Landivar',23)
print(f'Persona3: {persona3.nombre} {persona3.apellido} {persona3.edad}')

Persona4 = Persona('Maria','Correa',20)
Persona4.mostrarDetalle()

Persona.mostrarDetalle(persona1)


# class Persona:
#     def __init__(self, nombre, apellido, edad, *valores, **terminos):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.valores = valores
#         self.terminos = terminos

#     def mostrar_detalle(self):
#         print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')

# persona1 = Persona('Juan', 'Perez', 28, '44553322', 2, 3, 5, m='manzana', p='pera')
# persona1.mostrar_detalle()

# persona2 = Persona('Karla', 'Gomez', 30)
# persona2.mostrar_detalle()