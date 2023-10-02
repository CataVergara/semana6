class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def sonido(self):
        pass  


class Perro(Animal):
    def sonido(self):
        return "Guau"


class Gato(Animal):
    def sonido(self):
        return "Miau"


class Pajaro(Animal):
    def sonido(self):
        return "Pío pío"



perro = Perro("Firulais", 5)
gato = Gato("Garfield", 3)
pajaro = Pajaro("Piolín", 2)

print(perro.sonido())  
print(gato.sonido())   
print(pajaro.sonido())  