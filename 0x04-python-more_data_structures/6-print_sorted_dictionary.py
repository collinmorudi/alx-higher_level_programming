#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    odered_list = list(a_dictionary.keys())
    odered_list.sort()
    for i in odered_list:
        print("{}: {}".format(i, a_dictionary.get(i)))
