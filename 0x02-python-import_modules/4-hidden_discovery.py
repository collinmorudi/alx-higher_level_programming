#!/usr/bin/python3

import hidden_4 as hd

if __name__ == "__main__":
    names_list = dir(hd)[-3:]

    for name in names_list:
        print(name)
