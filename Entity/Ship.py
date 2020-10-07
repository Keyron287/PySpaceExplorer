from typing import final, List

from Entity.Component import Component
from Entity.Ship_Parts import AI, Hull
from Entity.Space_Entity import Space_entity
from Tick_Subjected import Tick_subjected


@final
class Ship(Space_entity, Tick_subjected):

    def __init__(self):
        self._ai: AI
        self._hull: Hull
        self._battery: float = self.hull.battery
        self._components: List[Component] = []
        self._cargo: List[Space_entity] = []
        super().__init__(None, None, size=self._hull.size, temperature=self._hull.temperature)

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
        return self._battery

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

    def pop_cargo(self):
        return self.cargo.pop(-1)

    def begin_tick(self):
        self._ai.begin_tick()
        pass

    def end_tick(self):
        self._ai.end_tick()
        pass

    def on_born(self):
        self._ai.on_born()
        pass

    def on_death(self):
        self._ai.on_death()
        pass
