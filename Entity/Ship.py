from typing import final, List

from Entity.Component import Component
from Entity.Ship_Parts import AI, Hull
from Entity.Space_Entity import Space_entity
from Tick_Subjected import Tick_subjected


class Battery_Exception(Exception):
    def __init__(self, message):
        super().__init__(message)


@final
class Ship(Space_entity, Tick_subjected):

    def __init__(self):
        self._ai: AI
        self._hull: Hull
        self._battery: float = self.hull.battery
        self._components: List[Component] = []
        self._cargo: List[Space_entity] = []
        super().__init__(size=self._hull.size, temperature=self._hull.temperature,
                         accessible_coordinates=self._hull.valid_coordinates)

    @property
    def ai(self):
        return self._ai

    @ai.setter
    def ai(self, value):
        self._ai = value

    @property
    def hull(self):
        return self._hull

    @hull.setter
    def hull(self, value):
        self._hull = value

    @property
    def battery(self):
        return self._battery, self._hull.battery

    @property
    def cargo(self):
        return self._cargo

    @property
    def components(self):
        return self._components

    def add_component(self, component):
        if len(self._components) + component.size < self._hull.max_components:
            component.parent = self
            self._components.append(component)

    def rem_component(self, component):
        self._components.remove(component)

    def push_cargo(self, cargo: Space_entity):
        if len(self._components) + cargo.size < self._hull.max_cargo:
            self.cargo.append(cargo)
        else:
            raise Exception("Cargo is full!")

    def pop_cargo(self):
        return self.cargo.pop(-1)

    def use_battery(self, quantity):
        if quantity < self._battery:
            raise Battery_Exception("Insufficient Energy")
        else:
            self._battery -= quantity

    def charge_battery(self, quantity):
        self._battery = min(self._hull.battery, self._battery+quantity)

    def begin_tick(self):
        self._ai.begin_tick()

    def end_tick(self):
        self._ai.end_tick()

    def on_born(self):
        self._ai.on_born()

    def on_death(self):
        self._ai.on_death()
