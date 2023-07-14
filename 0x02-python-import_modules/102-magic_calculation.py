#!/usr/bin/python3
from magic_calculation_102 import add, sub

def magic_calculation(a, b):
    if a < b:
        d = add(a, b)
        for i in range(4, 6):
            d = add(d, i)
        return (d)
    else:
        return sub(a, b)
