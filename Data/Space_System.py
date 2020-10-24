"""
Lo space system contiene tutte le space entityes
"""

from math import floor
from random import randrange, choice, random
from typing import List, Tuple

from Data.Celestial_bodies import Star, Planet, Moon, Asteroids, Celestial_body
from Data.Space_Entity import Coordinate, Space_Entity
from Data.Tick_Subjected import Tick_subjected


class Space_system:

    def __init__(self):
        self.planets = []
        self.entities = []
        self.connections = []
        self.__generate()
        stars = len(list(filter(lambda x: isinstance(x, Star), self.planets)))
        planets = len(list(filter(lambda x: isinstance(x, Planet), self.planets)))
        moons = len(list(filter(lambda x: isinstance(x, Moon), self.planets)))
        self.name = "System " + str(stars) + str(planets) + str(moons) + choice(
            ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])

    def __repr__(self):
        return self.name

    def __generate(self):
        bodies = randrange(1, 10)

        for a in range(bodies):
            gauss = (random() + random()) / 2
            gauss = floor(gauss * 3.99)
            b = None
            if gauss == 0 or a == 0:
                b = Star()
            elif gauss == 1:
                b = Planet()
            elif gauss == 2:
                b = Moon()
            elif gauss == 3:
                b = Asteroids()
            self.planets.append(b)

    def enter_system(self, entity: Space_Entity, position: tuple = None):
        if entity.system is not None:
            entity.system.exit_system(entity)
        self.entities.append(entity)
        entity.system = self
        entity.position = position or (self.planets[0], Coordinate.Space)

    def exit_system(self, entity):
        system = entity.system.entities
        system.remove(entity)

    def flight(self, ship, ascend=None, away=None):
        old_coordinates = ship.position
        new_body: Celestial_body = old_coordinates[0]
        new_coordinate = old_coordinates[1]
        body_index = self.planets.index(new_body)

        if ascend is not None and ascend:
            if new_coordinate.value + 1 > Coordinate.Space.value:
                raise Exception("Invalid position, outer space")
            else:
                nc = Coordinate(new_coordinate.value + 1)
                if nc in ship.accessible_coordinates:
                    new_coordinate = nc
                else:
                    raise Exception("Inaccessibile dalla nave")
        elif ascend is not None and not ascend:
            if new_coordinate.value - 1 < Coordinate.Landed.value:
                raise Exception("Invalid position, underground")
            else:
                nc = Coordinate(new_coordinate.value - 1)
                if nc in ship.accessible_coordinates:
                    new_coordinate = nc
                else:
                    raise Exception("Inaccessibile dalla nave")
        if away is not None and away and new_coordinate == Coordinate.space:
            if body_index + 1 >= len(self.planets):
                raise Exception("Invalid position, out of system! out of bounds+")
            else:
                new_body = self.planets[body_index + 1]
        elif away is not None and not away and new_coordinate == Coordinate.space:
            if body_index - 1 < 0:
                raise Exception("Invalid position, out of system! out of bounds-")
            else:
                new_body = self.planets[body_index - 1]

        ship.position = (new_body, new_coordinate)

    def get_sector_entities(self, coord: Tuple[Celestial_body, Coordinate], exclude=None) -> List[Space_Entity]:
        return list(filter(lambda x: x.position[0] == coord[0] and x.position[1] == coord[1] and x != exclude,
                           self.entities))

    def get_tick_active(self):
        return list(filter(lambda x: isinstance(x, Tick_subjected), self.entities))
