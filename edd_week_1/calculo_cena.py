#5 Pregunte cuanto costó la cena y la cantidad de invitados y luego calcule qué importe debería pagar cada uno


def calc_dinner(dinner_cost, guests):
    dinner_cost = int(dinner_cost)
    guests = int(guests)

    return dinner_cost / guests


def app():
    qst1 = 'Cuanto costo la cena?: '
    qst2 = 'Cuantos invitados asistieron a la cena?: '

    dinner_cost = input(qst1)
    guests = input(qst2)

    rsp = f'\nCada uno de los invitados deberia pagar { calc_dinner(dinner_cost,guests) }'
    print(rsp)


if __name__ == '__main__':
    app()
