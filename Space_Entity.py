from enum import Enum


class Coordinate(Enum):
    Landed = 0
    Orbit = 1
    Space = 2


class Space_Entity:

    def __init__(self, size=0, temperature=0, resources={}, accessible_coordinates=()):
        self.system = None
        self.position = ()
        self.size: int = size
        self.tempreature: float = temperature
        self.resources: dict = resources
        self.accessible_coordinates = accessible_coordinates

