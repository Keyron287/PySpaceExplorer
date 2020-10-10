from random import randrange
from typing import List

from Entity.Celestial_bodies import Star
from Entity.Component import Component
from Entity.Resources import Resource_box, Resources, Box_of_metal
from Entity.Space_Entity import Coordinate
from Tick_Subjected import Tick_action


class Extract_metal(Tick_action):

    def __init__(self, ship, planet, power):
        self.ship = ship
        self.planet = planet
        self.power = power

    def execute(self):
        if isinstance(self.ship.position[0], Star):
            raise Exception("You can't drill a Star")
        if self.ship.position[1] != Coordinate.Landed:
            raise Exception("You can't drill in the space")
        if randrange(1, 10) >= 7:
            metal = self.planet.resources[Resources.Metal]
            if metal == 0:
                raise Exception("There is no metal to extract")
            ext = min(metal, self.power)
            self.planet.resources[Resources.Metal] -= ext
            for a in range(ext):
                self.ship.push_cargo(Box_of_metal())


class Drill(Component):

    def __init__(self, power):
        super().__init__()
        self.power = power

    def get_size(self) -> int:
        return 1

    def get_energy_usage(self) -> float:
        return 1

    def use(self) -> List[Tick_action]:
        return [Extract_metal(self.parent, self.parent.position[0], self.power)]
