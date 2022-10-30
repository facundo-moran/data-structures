# 8. Escriba un programa que solicite al usuario el ingreso del nombre de tres ciudades
# del mundo que desea conocer y las almacene en una lista. Luego de haber
# ingresado los nombres, pregúntele si quiere añadir más ciudades. Si así lo de
# desea, permita el ingreso de más nombres hasta que la respuesta sea “no”.
# Cuando la respuesta sea “no” muestre por pantalla el número y listado de
# ciudades cargadas.


def is_valid_city_name(city_name: str) -> bool:
    city_name = city_name.strip().replace(" ", "")
    return city_name.isalpha() and len(city_name) > 2


def is_yes_or_no(asw: str) -> bool:
    asw = asw.lower().strip()
    return asw == 'yes' or asw == 'no'


def raise_on_false(val: bool) -> None:
    if not val:
        raise Exception


def app():
    print('Ingrese el nombre de 3 ciudades que desee conocer: ')
    city_names = []
    more_cities = True

    try:
        while more_cities:
            user_input = str(input('Insert a city name: \t'))

            raise_on_false(is_valid_city_name(user_input))
            city_names.append(user_input)

            if len(city_names) > 2:
                user_input = str(
                    input('Do you want to add more cities?: \tyes|no'))

                raise_on_false(is_yes_or_no(user_input))

                if user_input == 'no':
                    more_cities = not more_cities

    except:
        print("Input not valid!")


if __name__ == "__main__":
    app()
