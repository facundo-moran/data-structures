from datetime import date

from modelos.Genero import Genero
from modelos.Empresa import Empresa


class Videojuego:
    def __init__(self, titulo: str, genero: Genero, plataformas: list, descripcion: str, precio: float, empresa_desarrollo: Empresa, empresa_distribucion: Empresa, fecha_lanzamiento: date, ranking: float) -> None:
        if ranking < 0 or ranking > 10:
            raise ValueError('ranking out of range:', ranking)
        self.__titulo = titulo
        self.__genero = genero
        self.__plataformas = plataformas
        self.__descripcion = descripcion
        self.__precio = precio
        self.__empresa_desarrollo = empresa_desarrollo
        self.__empresa_distribucion = empresa_distribucion
        self.__fecha_lanzamiento = fecha_lanzamiento
        self.__ranking = ranking

    @property
    def fecha_lanzamiento(self):
        return self.__fecha_lanzamiento

    @property
    def titulo(self):
        return self.__titulo

    @property
    def genero(self):
        return self.__genero

    @property
    def empresa_desarrollo(self):
        return self.__empresa_desarrollo

    @property
    def empresa_distribucion(self):
        return self.__empresa_distribucion

    @property
    def plataformas(self):
        return self.__plataformas

    @property
    def ranking(self):
        return self.__ranking

    def __eq__(self, __o: object) -> bool:
        return self.__titulo == __o.titulo and self.__genero == __o.genero and self.__fecha_lanzamiento == __o.fecha_lanzamiento

    def __repr__(self) -> str:
        return f"Videojuego(titulo={self.__titulo}, genero={self.__genero}, plataformas={self.__plataformas}, descripcion={self.__descripcion}, precio={self.__precio}, empresa_desarrollo={self.__empresa_desarrollo}, empresa_distribucion={self.__empresa_distribucion}, fecha_lanzamiento={self.__fecha_lanzamiento}, ranking={self.__ranking})"

    def __str__(self) -> str:
        return f"Videojuego {self.__titulo} {self.__genero} {self.__plataformas} {self.__descripcion} {self.__precio} {self.__empresa_desarrollo} {self.__empresa_distribucion} {self.__fecha_lanzamiento} {self.__ranking}\n"
