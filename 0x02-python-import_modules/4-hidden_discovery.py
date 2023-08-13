#!/usr/bin/python3

import hidden_4 as hd

if __name__ == "__main__":
    names_list = dir(hd)

    for name in names_list:
        if not name.startswith("__"):
            print(name)
