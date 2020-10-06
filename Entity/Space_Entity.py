from enum import Enum

from typing import Tuple

from Space_System import Space_system


class Coordinate(Enum):
    Landed = 0
    Orbit = 1
    Space = 2
    Warping = 3


class Space_entity:

    def __init__(self):
        self.system: Space_system = None
        self.position_zero: Space_entity = None
        self.coordinates: Coordinate = Coordinate.Space
        self.size: int = 0
        self.tempreature: float = 0
        self.resources: list = []
