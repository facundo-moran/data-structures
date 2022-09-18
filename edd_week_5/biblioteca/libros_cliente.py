from modelos.Categoria import Categoria
from modelos.Libro import Libro
from modelos.Autor import Autor
import sys
sys.path.insert(0, "..")


def filtrar_por_anio(libros: list[Libro], anio: int) -> list:
    return [libro for libro in libros if libro.anio_publicacion == anio]


def filtrar_por_autor(libros: list[Libro], autor: Autor) -> list:
    return [libro for libro in libros if libro.autor == autor]


def filtrar_por_categoria(libros: list[Libro], cat: Categoria) -> list:
    return [libro for libro in libros if libro.categoria == cat]


def imprimir_libros(libros: list) -> None:
    for libro in libros:
        print(libro)


def app():

    libro1 = Libro(1, "titulo1", "autor1", "categoria1", 1990)
    libro2 = Libro(2, "titulo2", "autor2", "categoria2", 1995)
    libro3 = Libro(3, "titulo3", "autor3", "categoria3", 1990)
    libro4 = Libro(4, "titulo4", "autor3", "categoria1", 2596)
    libro5 = Libro(5, "titulo5", "autor3", "categoria1", 4856)

    print(f"\nImprimimos los libros")
    imprimir_libros([libro1, libro2, libro3, libro4, libro5])

    ANIO = 1990
    AUTOR = "autor3"
    CATEGORIA = "categoria1"
    
    print(f"\nfiltro por {ANIO}")
    for libro in filtrar_por_anio([libro1, libro2, libro3], ANIO):
        print(f"filtrar_por_anio ${ANIO}", libro)

    print(f"\nfiltro por {AUTOR}")
    for libro in filtrar_por_autor([libro1, libro2, libro3, libro4, libro5], AUTOR):
        print(f"filtrar_por_autor ${AUTOR}", libro)

    print(f"\nfiltro por {CATEGORIA}")
    for libro in filtrar_por_categoria([libro1, libro2, libro3, libro4, libro5], CATEGORIA):
        print(f"filtrar_por_categoria ${CATEGORIA}", libro)


if __name__ == "__main__":
    app()
