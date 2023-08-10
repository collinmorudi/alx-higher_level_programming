#!/usr/bin/bash

def print_last_digit(number):
    last_digit = 0
    if number < 0:
        last_digit = -1 * (number % -10)
    else:
        last_digit = number % 10

    print(last_digit, end="")
    return last_digit
