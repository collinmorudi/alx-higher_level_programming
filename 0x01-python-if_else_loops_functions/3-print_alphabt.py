#!/usr/bin/python3

for c in range(ord("a"), ord("z") + 1):
    if c == 101 or c == 113:
        continue
    print("{}".format(chr(c)), end="")
