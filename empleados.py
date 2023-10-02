class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def describir_rol(self):
        return "Empleado genérico"


class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, area):
        super().__init__(nombre, edad, salario)
        self.area = area

    def describir_rol(self):
        return f"Gerente en el área de {self.area}"


class Ingeniero(Empleado):
    def __init__(self, nombre, edad, salario, especialidad):
        super().__init__(nombre, edad, salario)
        self.especialidad = especialidad

    def describir_rol(self):
        return f"Ingeniero especializado en {self.especialidad}"


class Asistente(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)
        self.departamento = departamento

    def describir_rol(self):
        return f"Asistente en el departamento de {self.departamento}"


# Ejemplo de uso
gerente = Gerente("Gerente1", 35, 80000, "Ventas")
ingeniero = Ingeniero("Ingeniero1", 30, 60000, "Desarrollo")
asistente = Asistente("Asistente1", 25, 40000, "Recursos Humanos")

print(gerente.describir_rol())  
print(ingeniero.describir_rol())  
print(asistente.describir_rol())