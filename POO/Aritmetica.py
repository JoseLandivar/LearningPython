class Aritmetica:
    '''
    Clase Aritmetica para realizar Suma, Resta, etc.
    '''
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
        pass

    def Sumar(self):
        return self.operandoA + self.operandoB

    def Restar(self):
        return self.operandoA - self.operandoB

    def Multiplicar(self):
        return self.operandoA * self.operandoB

    def Dividir(self):
        return self.operandoA / self.operandoB
        
        

Aritmetica1 = Aritmetica(5,5)
print(f''' La suma es {Aritmetica1.Sumar()}')
    La resta es {Aritmetica1.Restar()}
    La multiplicacion es {Aritmetica1.Multiplicar()}
    La division es {Aritmetica1.Dividir()}''')
        