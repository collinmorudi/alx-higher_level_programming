#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    if roman_string == "":
        return 0
    num = 0
    dicti = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i, j in zip(roman_string, roman_string[1:]):
        if i not in dicti.keys():
            return 0
        elif dicti[i] >= dicti[j]:
            num += dicti[i]
        else:
            num -= dicti[i]
    num += dicti[roman_string[-1]]
    return num
