from random import randrange
from typing import List

from Celestial_bodies import Star
from Component import Component
from Resources import Resources, Box_of_metal
from Space_Entity import Coordinate
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


class Move_cargo(Tick_action):

    def __init__(self, origin, target):
        self.transfer = None
        self.origin = origin
        self.target = target

    def execute(self):
        self.transfer = self.origin.pop_cargo()
        self.target.push_cargo(self.transfer)


class Build_ship(Tick_action):

    def __init__(self, ship, project):
        self.ship = ship
        self.project = project

    def execute(self):
        self.ship.get_cargo(self.project.needed_components())
        ship = self.project.produce_ship()
        self.ship.system.enter_system(ship, self.ship.position)


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


class Mover(Component):

    def get_size(self) -> int:
        return 1

    def get_energy_usage(self) -> float:
        return 1

    def use(self, origin, target) -> List[Tick_action]:
        return [Move_cargo(origin, target)]


class Builder(Component):

    def set_project(self, project):
        super().__init__()
        self.project = project

    def get_size(self) -> int:
        return 10

    def get_energy_usage(self) -> float:
        return self.project.build_energy()

    def use(self) -> List[Tick_action]:
        return [Build_ship(self.parent, self.project)]
