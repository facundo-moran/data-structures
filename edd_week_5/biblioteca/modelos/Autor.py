class Autor:

    def __init__(self, apellido, nombre):
        self.__apellido = apellido
        self.__nombre = nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def nombre(self):
        return self.__nombre

    def __str__(self):
        return f"Autor: {self.__nombre}, {self.__apellido} "

    def __eq__(self, __o):
        return id(self) == id(__o)
