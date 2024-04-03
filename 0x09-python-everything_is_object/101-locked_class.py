#!/usr/bin/python3

"""
This moduel Defines a class with no class or object attribute
that control dynamically created instance attributes
"""


class LockedClass:
    """
    This class prevents a user from dinamically creating an
    instance variable unless the attribute is named "first_name"
    """
    __slots__ = "first_name"
