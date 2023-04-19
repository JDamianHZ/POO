# Clase principal
class Animal:
    def __init__(self, nombre, especie):
        self.__nombre = nombre
        self.__especie = especie
        self.__edad = 0

    # Métodos
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_especie(self):
        return self.__especie

    def set_especie(self, nueva_especie):
        self.__especie = nueva_especie

    def get_edad(self):
        return self.__edad

    def set_edad(self, nueva_edad):
        self.__edad = nueva_edad

    def hablar(self):
        pass

# Clase hija de Animal
class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Perro")

    # Métodos
    def hablar(self):
        return "¡Guau!"

# Clase hija de Animal
class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Gato")

    # Métodos
    def hablar(self):
        return "¡Miau!"

# Crear instancias de las clases
mi_perro = Perro("Fido")
mi_gato = Gato("Garfield")

# Acceder a los atributos de las instancias
print(mi_perro.get_nombre()) # Fido
print(mi_gato.get_especie()) # Gato

# Llamar a los métodos de las instancias
print(mi_perro.hablar()) # ¡Guau!
print(mi_gato.hablar()) # ¡Miau!