import re


def has_concordia_area_code(tel_number: str) -> bool:
    pattern = '(^.54)[0-9]{11}|(^0?345.)[0-9]{6}$|(^\(0345\))\s[0-9]{9}$'
    pattern_compiled = re.compile(pattern)

    return pattern_compiled.match(tel_number) and True
