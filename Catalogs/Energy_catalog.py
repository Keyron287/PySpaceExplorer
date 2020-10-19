from typing import List

from Celestial_bodies import Star, Celestial_body
from Component import Component, Category
from Resources import Resources
from Space_Entity import Coordinate
from Space_System import Space_system
from Tick_Subjected import Tick_action


class Transfer_energy(Tick_action):

    def __init__(self, origin_ship, target_ship, charge):
        self.origin = origin_ship
        self.target = target_ship
        self.charge = charge

    def msg(self) -> str:
        return "Transfering energy"

    def execute(self):
        self.origin.use_battery(self.charge)
        self.target.charge_battery(self.charge)


class Charge_battery(Tick_action):

    def __init__(self, target_ship, charge):
        self.ship = target_ship
        self.charge = charge

    def msg(self) -> str:
        return "Charging battery"

    def execute(self):
        self.ship.charge_battery(self.charge)


class Power_Bank(Component):
    def __init__(self):
        super().__init__()
        self.energy = 10

    def get_category(self):
        return Category.Energy

    def get_duration(self) -> int:
        return 1

    def get_size(self) -> int:
        return 1

    def get_energy_usage(self) -> float:
        return 0

    def use(self) -> List[Tick_action]:
        battery = self.parent.battery
        needed = min(self.energy, battery[1]-battery[0])
        self.energy -= needed
        return [Charge_battery(self.parent, needed)]


class Plug(Component):

    def __init__(self):
        super().__init__()
        self.energy_tranfer = 5

    def get_category(self):
        return Category.Energy

    def get_duration(self) -> int:
        return 2

    def get_size(self) -> int:
        return 1

    def get_energy_usage(self) -> float:
        return 0

    def use(self, origin, charge) -> List[Tick_action]:
        obattery = origin.battery
        tbattery = self.parent.battery
        needed = min(self.energy_tranfer, obattery[1]-obattery[0], tbattery[1] - tbattery[0])
        return [Transfer_energy(origin, self.parent, needed)]


class Solar_panel(Component):

    def get_category(self):
        return Category.Energy

    def get_duration(self) -> int:
        return 5

    def calculate_output(self, system: Space_system):
        ll = 0
        for a in system.planets:
            if isinstance(a, Star):
                ll += a.resources[Resources.Light]
        return ll

    def get_size(self) -> int:
        return 1

    def get_energy_usage(self) -> float:
        return 0

    def use(self) -> List[Tick_action]:
        self.system: Space_system = self.parent.system
        return [Charge_battery(self.parent, self.calculate_output(self.system))]


class Thermoelectric_generator(Component):

    def get_category(self):
        return Category.Energy

    def get_duration(self) -> int:
        return 10

    def calculate_output(self, coord: tuple):
        body: Celestial_body = coord[0]
        distance: Coordinate = coord[1]
        temp = body.tempreature
        return temp/(1000*(10**distance.value))

    def get_size(self) -> int:
        return 5

    def get_energy_usage(self) -> float:
        return 0

    def use(self) -> List[Tick_action]:
        coords = self.parent.position
        return [Charge_battery(self.parent, self.calculate_output(coords))]

