# utils.py
from itertools import cycle


def verificar_rut(rut):
    rut = rut.replace('.', '').upper().strip()
    if '-' not in rut or not rut.split('-')[0].isdigit():
        return False
    cuerpo, dv = rut.split('-')
    dv = dv.upper()

    reversed_digits = map(int, reversed(str(cuerpo)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    dvReal = (-s) % 11

    if dvReal == 10:
        dvReal = 'K'

    return str(dvReal) == dv


