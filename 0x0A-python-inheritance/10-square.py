#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
Rectangle = __import__('9-rectangle').Rectangle
        
        
class Square(Rectangle):
        """derive a square class"""
        def __int__(self, size):
            """initialization"""
            self.integer_validator("size", size)
            self.__size = size
            super().__init__(size, size)

        def area(self):
            return self.__size * self.__size
