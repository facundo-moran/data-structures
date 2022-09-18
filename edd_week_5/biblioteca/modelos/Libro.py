
class Libro:

    def __init__(self, num_inventario, titulo, autor, categoria, anio_publicacion):
        self.__num_inventario = num_inventario
        self.__titulo = titulo
        self.__autor = autor
        self.__categoria = categoria
        self.__anio_publicacion = anio_publicacion

    @property
    def num_inventario(self):
        return self.__num_inventario

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def categoria(self):
        return self.__categoria

    @property
    def anio_publicacion(self):
        return self.__anio_publicacion

    def __str__(self) -> str:
        return f"Libro: {self.__titulo}, {self.__categoria}, {self.__autor}, {self.__num_inventario}, {self.__anio_publicacion}"

    def __eq__(self, __o):
        return id(self) == id(__o)
