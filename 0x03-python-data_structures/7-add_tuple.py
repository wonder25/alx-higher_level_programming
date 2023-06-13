#!/usr/bin/python3

def add_tuple(tuple_a =(), tuple_b=()):
    if len(tuple_a) == 0:
        a = 0
        b = 0
    elif (len(tuple_a) == 1):
        a = tuple_a[0]
        b = 0
    else:
        a = tuple_a[0]
        b = tuple_a[1]

    if len(tuple_b) == 0:
        e = 0
        f = 0
    elif (len(tuple_b) == 1):
        e = tuple_b[0]
        f = 0
    else:
        e = tuple_b[0]
        f = tuple_b[1]

    new_tuple = (a + e, b + f)

    return new_tuple
