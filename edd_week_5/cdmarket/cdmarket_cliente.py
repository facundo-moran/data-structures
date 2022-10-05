from datetime import datetime

from modelos.VideojuegosAdmin import VideojuegosAdmin
from modelos.Empresa import Empresa
from modelos.Genero import Genero
from modelos.Videojuego import Videojuego
from modelos.Plataforma import Plataforma


def app():
    empresa_1 = Empresa('Meta')
    empresa_1_dist = Empresa('Instagram')
    empresa_2 = Empresa('Google')
    empresa_2_dist = Empresa('Globant')
    empresa_3 = Empresa('Mercadolibre')
    empresa_3_dist = Empresa('Uber')
    empresa_4 = Empresa('Idea')
    empresa_4_dist = Empresa('Apple')
    empresa_5 = Empresa('Starbucks')
    empresa_5_dist = Empresa('Netflix')

    pc = Plataforma('pc', False)
    ps4 = Plataforma('ps4', False)
    xbox_one = Plataforma('xboxone', False)
    switch = Plataforma('switch', True)
    ps5 = Plataforma('ps5', False)
    xsx = Plataforma('xsx', False)

    moonscars = Videojuego('Moonscars', Genero.OTRO,
                           list([pc, ps4, xbox_one, switch, ps5, xsx]), 'Moonscars description', 199.9, empresa_1, empresa_1_dist, datetime.now().date(), 9)

    fist = Videojuego('F.I.S.T', Genero.LUCHA,
                      list([pc, ps4, switch, ps5]), 'F.I.S.T description', 500.0, empresa_2, empresa_2_dist, datetime.now().date(), 7.5)

    sonic = Videojuego('Sonic Frontiers', Genero.CARRERAS,
                       list([pc, ps4, xbox_one, switch, ps5, xsx]), 'Sonic Frontiers description', 150.5, empresa_4, empresa_4_dist, datetime.now().date(), 6)

    cuphead = Videojuego('Cuphead', Genero.AVENTURA_ANIMADA,
                         list([pc, ps4, xbox_one, switch]), 'Cuphead description', 330.0, empresa_3, empresa_3_dist, datetime.now().date(), 8)

    super_mario_odisea = Videojuego('Super Mario Odyssey', Genero.CARRERAS,
                                    list([switch]), 'Super Mario Odyssey description', 330.0, empresa_5, empresa_5_dist, datetime.now().date(), 4)

    admin = VideojuegosAdmin()

    print('\nstr:', admin.__str__())

    admin.agregar(sonic)
    admin.agregar(cuphead)
    admin.agregar(super_mario_odisea)
    admin.agregar(fist)
    admin.agregar(moonscars)
    print('\nagregar:\n', admin.__str__())

    print('\nfiltrar por desarrolladora:\n',
          admin.filtrar_por_desarrolladora(empresa_3))

    print('\nfiltrar por distribuidora:\n',
          admin.filtrar_por_distribuidora(empresa_3_dist))

    print('\nfiltrar por genero:\n', admin.filtrar_por_genero(Genero.CARRERAS))

    print('\nCantidad por plataforma:\n', admin.cantidad_por_plataforma())

    admin.ordenar_titulo()
    print('\nordenar titulo:\n', admin.__str__())

    admin.ordenar_mejores_primero()
    print('\nordenar mejores primeros:\n', admin.__str__())


if __name__ == "__main__":
    app()
