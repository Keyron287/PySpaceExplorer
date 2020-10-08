from math import floor
from random import randrange, random
from typing import List, Tuple

from Entity.Celestial_bodies import Star, Planet, Moon, Asteroids, Celestial_body
from Entity.Space_Entity import Coordinate, Space_entity


class Space_system:

    def __init__(self):
        self.planets: List[Celestial_body] = []
        self.entities: List[Space_entity] = []
        self.connections: List[Space_system] = []
        self.__generate()

    def __generate(self):
        bodies = randrange(1, 15)

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

    def enter_system(self, entity: Space_entity):
        entity.system.exit_system(entity)
        self.entities.append(entity)
        entity.position = (self.planets[0], Coordinate.Space)

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

    def get_sector_entities(self, coord: Tuple[Celestial_body, Coordinate]) -> List[Space_entity]:
        return list(filter(lambda x: x.position[0] == coord[0] and x.position[1] == coord[1], self.entities))
