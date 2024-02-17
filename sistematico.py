class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        print(f"el rersultado es {self.base * self.altura}")

sistem1 = Rectangulo(11, 5)
sistem1.calcular_area()
    


