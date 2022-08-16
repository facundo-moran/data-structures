# Pregunte cuanto costó la cena y la cantidad de invitados y luego calcule qué importe debería pagar cada uno


def calculo_cena(costo_cena, cant_invitados=1):
    costo_cena = int(costo_cena)
    cant_invitados = int(cant_invitados)

    return costo_cena / cant_invitados


def app():
    qst1 = 'Cuanto costo la cena?: '
    qst2 = 'Cuantos invitados asistieron a la cena?: '

    costo_cena = input(qst1)
    cant_invitados = input(qst2)

    rsp = f'\nCada uno de los invitados deberia pagar {calculo_cena(costo_cena,cant_invitados)}'
    print(rsp)


app()


