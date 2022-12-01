#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    user_input = argv[1:]
    size = len(user_input)
    print("{:d} {:s}{:s}".
          format(size,
                 "arguments" if (size) is not 1 else "argument",
                 "." if (size) is 0 else ":"))
    for idx, arg in enumerate(user_input):
        print("{:d}: {:s}".format(idx + 1, arg))
