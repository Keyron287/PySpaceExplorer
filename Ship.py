from typing import final, List

from Component import Component, Category
from Ship_Parts import AI, Hull
from Space_Entity import Space_Entity


class Battery_Exception(Exception):
    def __init__(self, message):
        super().__init__(message)


@final
class Ship(Space_Entity):

    def __init__(self, ai, hull):
        self._ai: AI = ai
        self._ai.ship = self
        self._hull: Hull = hull
        self._battery: float = self.hull.battery
        self._components: List[Component] = []
        self._cargo: List[Space_Entity] = []
        super().__init__(size=self._hull.size, temperature=self._hull.temperature,
                         accessible_coordinates=self._hull.valid_coordinates)

    @property
    def current_action_msg(self):
        try:
            return self.current_action.msg()
        except AttributeError:
            return "Nothing"

    def __repr__(self):
        return self._hull.__class__.__name__ + "(" + self.ai.ai_pourpose() + ")["+self.current_action_msg+"]"

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

    def get_components(self, cat: Category, cls=None):
        if cls is None:
            return list(filter(lambda x: x.get_category() == cat, self._components))
        else:
            return list(filter(lambda x: x.get_category() == cat and isinstance(x, cls), self._components))

    def has_component(self, cls):
        for a in self._components:
            if isinstance(a, cls):
                return True
        return False

    def add_component(self, component):
        if len(self._components) + component.get_size() <= self._hull.max_components:
            component.parent = self
            self._components.append(component)
        else:
            raise Exception("Not enough space for component")

    def rem_component(self, component):
        self._components.remove(component)

    def push_cargo(self, cargo: Space_Entity):
        if len(self._components) + cargo.size < self._hull.max_cargo:
            self.cargo.append(cargo)
        else:
            raise Exception("Cargo is full!")

    def pop_cargo(self):
        return self.cargo.pop(-1)

    def get_cargo(self, needed: list):
        if set(needed).issubset(set(self._cargo)):
            self._cargo = [x for x in self._cargo if x not in needed]
            return needed
        else:
            raise Exception("Not enough materials")

    def use_battery(self, quantity):
        if quantity < self._battery:
            raise Battery_Exception("Insufficient Energy")
        else:
            self._battery -= quantity

    def charge_battery(self, quantity):
        self._battery = min(self._hull.battery, self._battery + quantity)

    def fly(self, ascend=None, away=None):
        self.system.flight(self, ascend, away)

    def begin_tick(self):
        self._ai.begin_tick()

    def end_tick(self):
        self._ai.end_tick()

    def on_born(self):
        self._ai.on_born()

    def on_death(self):
        self._ai.on_death()
