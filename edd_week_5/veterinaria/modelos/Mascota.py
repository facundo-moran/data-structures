class Mascota:

    ANIO_ACTUAL = 2022

    def __init__(self, nro_registro, nombre, raza, anio_nacimiento, amo) -> None:
        self.__nro_registro = nro_registro
        self.__nombre = nombre
        self.__raza = raza
        self.__anio_nacimiento = anio_nacimiento
        self.__amo = amo
        self.__edad = 2022 - anio_nacimiento

    @classmethod
    def set_anio_actual(cls, anio):
        cls.ANIO_ACTUAL = anio if anio > 0 else 2022

    @property
    def edad(self):
        return self.__edad

    @property
    def nro_registro(self):        
        return self.__nro_registro 

    @property
    def nombre(self):
        return self.__nombre

    @property
    def raza(self):
        return self.__raza

    @property
    def anio_nacimiento(self):
        return self.__anio_nacimiento

    @property
    def amo(self):
        return self.__amo

    def __eq__(self, __o):
        return self.__nombre == __o.nombre and self.__amo == __o.amo

    def __repr__(self) -> str:
        return f"Mascota(nro_registro={self.__nro_registro}, nombre={self.__nombre}, raza={self.__raza}, anio_nacimiento={self.__anio_nacimiento}, amo={self.__amo})"

    def __str__(self) -> str:
        return f"Mascota {self.__nro_registro}, {self.__nombre}, {self.__raza}, {self.__anio_nacimiento}, {self.__amo}, {self.__edad})"
