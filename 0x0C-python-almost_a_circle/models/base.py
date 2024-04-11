#!/usr/bin/python3

""" Base class module to manage all other classess IDs """

class Base:
    """ Base Class for all future classess """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

