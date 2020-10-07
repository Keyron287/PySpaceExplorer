from enum import Enum
from typing import Tuple

from Space_System import Space_system


class Coordinate(Enum):
    Landed = 0
    Orbit = 1
    Space = 2


class Space_entity:

    def __init__(self, name, size=0, temperature=0, resources=[]):
        self.system: Space_system
        self.name: str = name
        self.size: int = size
        self.tempreature: float = temperature
        self.resources: list = resources

