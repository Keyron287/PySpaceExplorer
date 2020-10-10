from typing import List

from Entity.Celestial_bodies import Resources
from Entity.Component import Component
from Tick_Subjected import Tick_action


class Scan_connections(Tick_action):

    def __init__(self, ship, component):
        self.system = ship.system
        self.component = component

    def execute(self):
        self.component.scanned = self.system.connections


class Scan_sectior(Tick_action):
    def __init__(self, ship, component, position=None):
        self.ship = ship
        self.system = ship.system
        self.position = position or self.ship.position
        self.component = component

    def execute(self):
        self.component.scanned = self.system.get_sector_entities(self.position, exclude=self.ship)


class Scan_Metal(Tick_action):
    def __init__(self, ship, component, target):
        self.ship = ship
        self.target = target
        self.component = component

    def execute(self):
        self.component.scanned = self.target.resources[Resources.Metal]


class Telescope(Component):

    def __init__(self, parent):
        super().__init__(parent)
        self.scanned = []

    def get_size(self) -> int:
        return 3

    def get_energy_usage(self) -> float:
        return 5

    def use(self, ship) -> List[Tick_action]:
        return [Scan_connections(ship, self)]


class Lidar(Component):

    def __init__(self, parent):
        super().__init__(parent)
        self.scanned = []

    def get_size(self) -> int:
        return 2

    def get_energy_usage(self) -> float:
        return 5

    def use(self, ship, position=None) -> List[Tick_action]:
        return [Scan_sectior(ship, self, position)]


class Metal_detector(Component):

    def __init__(self, parent):
        super().__init__(parent)
        self.scanned = []

    def get_size(self) -> int:
        return 2

    def get_energy_usage(self) -> float:
        return 5

    def use(self, ship, position=None) -> List[Tick_action]:
        return [Scan_sectior(ship, self, position)]