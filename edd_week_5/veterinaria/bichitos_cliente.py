from modelos.Especie import Especie
from modelos.Mascota import Mascota
from modelos.Persona import Persona
from modelos.Raza import Raza


def max_mascotero(mascotas: list[Mascota]):
    mascoteros = set(map(lambda mascota: mascota.amo, mascotas))
    mascoteros_dict = dict.fromkeys(mascoteros,0)

    for mascota in mascotas:
        mascoteros_dict[mascota.amo] += 1 
    
    return max( mascoteros_dict, key = lambda k: mascoteros_dict[k])


def filtrar_por_especie(mascotas: list[Mascota], especie: Especie) -> list[Mascota]:
    return filter(lambda mascota: mascota.raza.especie == especie, mascotas)


def filtrar_gerontes(mascotas: list[Mascota]) -> list:
    return filter(lambda mascota: mascota.edad > 13, mascotas)


def imprimir(mascotas: list[Mascota]) -> None:
    for mascota in mascotas:
        print(mascota)


def app():

    amo1 = Persona("apellido1", "nombre1", "123412")
    amo2 = Persona("apellido2", "nombre2", "134134")
    amo3 = Persona("apellido3", "nombre3", "345345")
    amo4 = Persona("apellido4", "nombre4", "235235")
    amo5 = Persona("apellido5", "nombre5", "457547")

    especie1 = Especie("perros")
    especie2 = Especie("gatos")
    especie3 = Especie("aves")

    raza1 = Raza("Akina inu", especie1)
    raza2 = Raza("Canario", especie3)
    raza3 = Raza("Oriental", especie2)
    raza4 = Raza("Border Collie", especie1)
    raza5 = Raza("Persa", especie2)

    mascota1 = Mascota(1, "nombre1", raza2, 2005, amo3)
    mascota2 = Mascota(2, "nombre2", raza1, 2017, amo2)
    mascota3 = Mascota(3, "nombre3", raza2, 2008, amo4)
    mascota4 = Mascota(4, "nombre4", raza3, 2009, amo4)
    mascota5 = Mascota(5, "nombre5", raza2, 2015, amo5)
    mascota6 = Mascota(6, "nombre6", raza2, 2020, amo1)
    mascota7 = Mascota(7, "nombre7", raza5, 2018, amo1)
    mascota8 = Mascota(8, "nombre8", raza4, 2021, amo1)

    mascotas = [mascota1, mascota2, mascota3, mascota4,
                mascota5, mascota6, mascota7, mascota8]

    print("\nMostramos las mascotas")
    imprimir(mascotas)

    print(f"\nFiltramos por especie={especie3}")
    for mascota in filtrar_por_especie(mascotas, especie3):
        print(f"filtrado por {especie3}", mascota)

    EDAD_MAYOR_A = 13

    print(f"\nFiltramos por edad > {EDAD_MAYOR_A} ")
    for mascota in filtrar_gerontes(mascotas):
        print(f"filtrado por edad > {EDAD_MAYOR_A}", mascota)

    print("\nPersona mas mascotera")
    print(max_mascotero(mascotas))


if __name__ == "__main__":
    app()
