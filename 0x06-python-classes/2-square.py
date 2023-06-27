#!/usr/bin/python3
"""square class """


class Square:
    """represent a square class"""
    def __init__(self, size=0):
        try:
            if not isinstance(size, int):
                raise TypeError
            elif size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
        self.__size = size
