class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar (self):
        print(f"hola, soy {self.nombre} y tengo {self.edad} año.")
        

persona1 = Persona("dmg",30)
persona1.saludar ()
esposa = Persona("nanchi",31)
esposa.saludar ()

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    def estudiar(self):
        print(f"{self.nombre} esta estudiando el grado de {self.grado}.")

estudiante1 = Estudiante("Gabriela", 29, "Maestria")
estudiante1.saludar()
estudiante1.estudiar()



