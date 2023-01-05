#!/usr/bin/python3
"""
This is a module that containts a class that does not
allow dynmaically created attributes
"""


class LockedClass:
    __slots__ = 'first_name'
