from typing import List

from Data.Component import Component, Category
from Data.Space_Entity import Space_Entity
from Data.Space_System import Space_system
from Data.Tick_Subjected import Tick_action


class Fly(Tick_action):

    def __init__(self, ship: Space_Entity, ascend=None, away=None):
        self.ship = ship
        self.ascend = ascend
        self.away = away

    def execute(self):
        self.ship.fly(self.ascend, self.away)

    def msg(self) -> str:
        return "Flying"


class Warp(Tick_action):

    def __init__(self, ship: Space_Entity, destination: Space_system):
        self.ship = ship
        self.destination = destination

    def msg(self) -> str:
        return "Warping"

    def execute(self):
        self.destination.enter_system(self.ship)


class Flyer(Component):

    def get_category(self):
        return Category.Propulsion

    def get_size(self) -> int:
        return 2

    def get_energy_usage(self) -> float:
        return 5

    def get_duration(self) -> int:
        return 2

    def use(self, ascend, away) -> List[Tick_action]:
        return [Fly(self.parent, ascend, away)]


class Warper(Component):
    def get_category(self):
        return Category.Propulsion

    def get_size(self) -> int:
        return 10

    def get_energy_usage(self) -> float:
        return 50

    def get_duration(self) -> int:
        return 5

    def use(self, destination_system) -> List[Tick_action]:
        return [Warp(self.parent, destination_system)]
