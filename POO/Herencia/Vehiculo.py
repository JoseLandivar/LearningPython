class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        pass

        def __str__(self):
            return f'{self.color}{self.ruedas}' 

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'{self.velocidad}' 

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'{self.tipo}' 


movil1 = Bicicleta('Azul',4/4,'Montaña')

print(movil1.color)


