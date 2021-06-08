'''
A continuación os vamos a dejar crear un ejercicio para calcular el área de un rectángulo.
les vamos a dejar crear una nueva clase.
Esta clase se va a llamar rectangulo y va a tener dos atributos el atributo de altura y el atributo
de base, y posteriormente va a tener un método llamado calcular área y el área se calcula con la siguientefórmula.
Vamos a calcular la base por la altura y eso nos debe dar el área del rectángulo.
Sin embargo, estos valores de base de altura los debe de proporcionar el usuario, así que no se programa.
La ejecución debe ser como sigue.
Vamos a solicitar proporciona la base. Proporcionamos algún valor. Por ejemplo. 4. Y posteriormente la altura.
Por ejemplo el valor de 5. Y entonces Aldara Inter nos debe de regresar el cálculo del área de un rectángulo.
En este caso el valor de 20. Ya que el cálculo del área es 4 por 5. Nos da el valor de 20.
Así que el ejercicio que les dejamos realizar utilizando el concepto de clases que hemos estudiado hasta
el momento.
'''
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def formula(self):
        return self.base * self.altura


base = int(input('Ingrese Base: '))
altura = int(input('Ingrese Altura: '))

resultado = Rectangulo(base,altura)
print(f'El area es; {resultado.formula()}')