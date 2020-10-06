from typing import final

from Entity.Ship_AI import Ship_AI
from Entity.Space_Entity import Space_entity
from Tick_Subjected import Tick_subjected


@final
class Ship(Space_entity, Tick_subjected):

    def __init__(self):
        super().__init__()
        self._ai: Ship_AI = None
        self._hull = None
        self._battery = None
        self._propulsion = None
        self._components = []

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
    def generator(self):
        return self._battery

    @property
    def propulsion(self):
        return self._propulsion

    @propulsion.setter
    def propulsion(self, value):
        self._propulsion = value

    def add_component(self, component):
        if len(self._components) < self._hull.max_components:
            component.parent = self
            self._components.append(component)

    def rem_component(self, component):
        self._components.remove(component)

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
