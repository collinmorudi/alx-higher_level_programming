#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for ch in str:
        if 97 <= ord(ch) <= 122:
            x = ord(ch) - 32
            upper += chr(x)
            continue
        upper += ch
    print("{}".format(upper))
