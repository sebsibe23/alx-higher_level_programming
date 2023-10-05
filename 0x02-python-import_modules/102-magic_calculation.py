#!/usr/bin/python3


def magic_calculation(e, h):
    from magic_calculation_102 import add, sub

    if e < h:
        z = add(e, h)
        for s in range(4, 6):
            z = add(z, s)
        return (z)

    else:
        return(sub(e, h))
