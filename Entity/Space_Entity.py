from enum import Enum
from typing import Tuple

from Entity.Celestial_bodies import Celestial_body
from Space_System import Space_system


class Coordinate(Enum):
    Landed = 0
    Orbit = 1
    Space = 2


class Space_entity:

    def __init__(self, name, size=0, temperature=0, resources={}, accessible_coordinates=()):
        self.system: Space_system = None
        self.position: Tuple[Celestial_body, Coordinate] = ()
        self.name: str = name
        self.size: int = size
        self.tempreature: float = temperature
        self.resources: dict = resources
        self.accessible_coordinates = accessible_coordinates
