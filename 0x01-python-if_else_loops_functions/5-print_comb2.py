#!/usr/bin/bash

for i in range(100):
    if i == 99:
        print("{}".format(i))
    else:
        print("0{}".format(i) if i < 10 else "{}".format(i), end=", ")
