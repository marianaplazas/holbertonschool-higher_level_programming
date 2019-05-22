#!/usr/bin/python3
class MagicClass:
    def __init__(self, radius):
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return ((self.__radius * self.__radius) * math.pi)

    def circumference(self):
        return 2 * math.pi * self.__radius
