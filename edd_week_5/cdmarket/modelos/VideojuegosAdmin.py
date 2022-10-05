from modelos.Genero import Genero
from modelos.Empresa import Empresa
from modelos.Videojuego import Videojuego
from modelos.abstract.VideojuegoAdminAbstract import VideojuegosAdminAbstract


class VideojuegosAdmin(VideojuegosAdminAbstract):

    def __str__(self) -> str:
        return "".join(self.videojuegos.__str__())

    def agregar(self, videojuego: Videojuego) -> None:
        self.videojuegos.append(videojuego)

    def filtrar_por_desarrolladora(self, desarrolladora: Empresa) -> list:
        videojuegos = list(
            filter(lambda v: v.empresa_desarrollo == desarrolladora, self.videojuegos))

        return videojuegos

    def filtrar_por_distribuidora(self, distribuidora: Empresa) -> list:
        videojuegos = list(
            filter(lambda v: v.empresa_distribucion == distribuidora, self.videojuegos))

        return videojuegos

    def filtrar_por_genero(self, genero: Genero) -> list:
        videojuegos = list(
            filter(lambda v: v.genero == genero, self.videojuegos))

        return videojuegos

    def cantidad_por_plataforma(self) -> list:

        global counter, cant_juegos_plataforma

        cant_juegos_plataforma = {}
        counter = 1

        for vj in self.videojuegos:
            for p in vj.plataformas:
                if p in cant_juegos_plataforma:
                    cant_juegos_plataforma[p] = cant_juegos_plataforma[p] + 1
                else:
                    cant_juegos_plataforma[p] = counter

        plataformas = list(zip(cant_juegos_plataforma.keys(),
                           cant_juegos_plataforma.values()))
        return plataformas

    def ordenar_titulo(self) -> None:
        self.videojuegos.sort(key=lambda vj: vj.titulo)

    def ordenar_mejores_primero(self) -> None:
        self.videojuegos.sort(key=lambda vj: vj.ranking, reverse=True)
