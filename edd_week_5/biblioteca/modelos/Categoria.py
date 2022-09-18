class Categoria:

    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    def __str__(self):
        return f"Autor: {self.__nombre}"

    def __eq__(self, __o):
        return id(self) == id(__o)