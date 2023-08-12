#!/usr/bin/python3

def no_c(my_string):
    new_str = ""

    for el in my_string:
        if el in "Cc":
            continue
        new_str += el

    return new_str
