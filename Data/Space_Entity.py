"""
La classe Space_Entity rappresenta ogni entità che sta all'interno dello spazio
"""

from abc import ABC
from enum import Enum

from Data.Tick_Subjected import Tick_subjected


class Coordinate(Enum):
    """Lista delle coordinate che può assumere una entity"""
    Landed = 0
    Orbit = 1
    Space = 2


class Space_Entity(Tick_subjected, ABC):

    def __init__(self, size=0, temperature=0, resources=None, accessible_coordinates=()):
        super().__init__()
        if resources is None:
            resources = {}
        self.system = None
        self.position = ()
        self.size: int = size
        self.tempreature: float = temperature
        self.resources: dict = resources
        self.accessible_coordinates = accessible_coordinates
