#!/usr/bin/python3
"""
Module 3-is_kind_of_class
Contains method is_kind_of_class that returns True if object is an
instance of class that it inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of class that it inherited from
    """
    return isinstance(obj, a_class)
