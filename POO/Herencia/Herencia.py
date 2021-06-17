# Clase Padre

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'{self.nombre}{self.edad}'        

# Clase Hija

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'{self.sueldo} {super().__str__()}'

Empleado1 = Empleado('Jose', 25, 11000)

#print(Empleado1.nombre)
#print(Empleado1.edad)
#print(Empleado1.sueldo)