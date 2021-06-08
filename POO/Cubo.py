#Calcular el volumen de un cubo

class Cubo:
    def __init__(self, alto, ancho, largo):
        self.alto = alto
        self.ancho = ancho
        self.largo = largo
        pass
    
    def calculo(self):
        return self.alto * self.ancho * self.largo

alto = int(input('Ingrese Alto: '))
ancho = int(input('Ingrese Ancho: '))
largo = int(input('Ingrese Largo: '))


resultado = Cubo(alto,ancho,largo)

print(f'El resultado es: {resultado.calculo()}')