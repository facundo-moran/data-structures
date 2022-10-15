from modules.tel_concor_reg import has_concordia_area_code


def app():
    print(
        f'(0345) 154123456 (válido). {has_concordia_area_code("(0345) 154123456")}')
    print(
        f'+5493454123456 (válido). {has_concordia_area_code("+5493454123456")}')
    print(f'3454123456 (válido). {has_concordia_area_code("3454123456")}')
    print(
        f'+54011123456 (válido). {has_concordia_area_code("+54011123456")}')
    print(f'34564123456 (válido). {has_concordia_area_code("34564123456")}')
    print(f'3454183422 (válido). {has_concordia_area_code("3454183422")}')
    print(
        f'+5493454183422 (válido). {has_concordia_area_code("+5493454183422")}')
    print(
        f'(0345) 154183422 (válido). {has_concordia_area_code("(0345) 154183422")}')


if __name__ == "__main__":
    app()
