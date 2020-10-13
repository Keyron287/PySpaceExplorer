from enum import Enum
from typing import Tuple

import Celestial_bodies
import Space_System
from Resources import Resources


class Coordinate(Enum):
    Landed = 0
    Orbit = 1
    Space = 2


class Space_entity:

    def __init__(self, name, size=0, temperature=0, resources={}, accessible_coordinates=()):
        self.system: Space_System.Space_system = None
        self.position: Tuple[Celestial_bodies.Celestial_body, Coordinate] = ()
        self.name: str = name
        self.size: int = size
        self.tempreature: float = temperature
        self.resources: dict = resources
        self.accessible_coordinates = accessible_coordinates


class Celestial_body(Space_entity):

    def __init__(self, name, orbit=None):
        super().__init__(name)
        self.orbit = orbit


class Resource_box(Space_entity):

    def __init__(self, base_resource: Resources):
        super().__init__(self.__class__.__name__, size=1)
        self.base = base_resource
