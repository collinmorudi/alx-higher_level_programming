#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a, b = 0, 0
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a > 1 and len_b > 1:
        a = tuple_a[0] + tuple_b[0]
        b = tuple_a[1] + tuple_b[1]
    elif len_a > 1 and len_b == 1:
        a = tuple_a[0] + tuple_b[0]
        b = tuple_a[1]
    elif len_a == 1 and len_b > 1:
        a = tuple_a[0] + tuple_b[0]
        b = tuple_b[1]
    elif len_a == 1 and len_b == 1:
        a = tuple_a[0] + tuple_b[0]
    elif len_a > 1 and len_b == 0:
        a = tuple_a[0]
        b = tuple_a[1]
    elif len_a == 1 and len_b == 0:
        a = tuple_a[0]
    elif len_a == 0 and len_b > 1:
        a = tuple_b[0]
        b = tuple_b[1]
    elif len_a == 0 and len_b == 1:
        a = tuple_b[0]

    return a, b
