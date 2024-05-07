class Produccion:
    def calcular_produccion(self):
        pass

class Cultivo:
    def __init__(self, nombre, tipo, area, rendimiento):
        self.nombre = nombre
        self.tipo = tipo
        self.area = area
        self.rendimiento = rendimiento

class Animal:
    def __init__(self, especie, raza, edad, peso):
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.peso = peso

class Granja:
    def __init__(self):
        self.cultivos = []
        self.animales = []

    def agregar_cultivo(self, cultivo):
        self.cultivos.append(cultivo)

    def eliminar_cultivo(self, nombre_cultivo):
        for cultivo in self.cultivos:
            if cultivo.nombre == nombre_cultivo:
                self.cultivos.remove(cultivo)

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def eliminar_animal(self, especie_animal):
        for animal in self.animales:
            if animal.especie == especie_animal:
                self.animales.remove(animal)

    def calcular_produccion_granja(self):
        produccion_cultivos = sum(cultivo.rendimiento * cultivo.area for cultivo in self.cultivos)
        produccion_animales = sum(animal.peso for animal in self.animales)
        return produccion_cultivos + produccion_animales

# Ejemplo de uso del sistema
granja_ucundinamarca = Granja()

# Agregar cultivos
cultivo_maiz = Cultivo("Maíz", "Grano", 100, 20)
cultivo_trigo = Cultivo("Trigo", "Grano", 150, 30)
granja_ucundinamarca.agregar_cultivo(cultivo_maiz)
granja_ucundinamarca.agregar_cultivo(cultivo_trigo)

# Agregar animales
animal_vaca = Animal("Vaca", "Holstein", 5, 400)
animal_cerdo = Animal("Cerdo", "Yorkshire", 2, 200)
granja_ucundinamarca.agregar_animal(animal_vaca)
granja_ucundinamarca.agregar_animal(animal_cerdo)

# Calcular producción total
produccion_total = granja_ucundinamarca.calcular_produccion_granja()
print("Producción total de la granja:", produccion_total)
