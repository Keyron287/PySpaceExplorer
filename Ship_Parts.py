from abc import ABC

from Tick_Subjected import Tick_subjected


class AI(Tick_subjected):
    def begin_tick(self):
        pass

    def end_tick(self):
        pass

    def on_born(self):
        pass

    def on_death(self):
        pass


class Hull(ABC):

    def __init__(self, size, max_components, max_cargo, valid_coordinates, battery, temperature):
        self.size = size
        self.max_components = max_components
        self.max_cargo = max_cargo
        self.valid_coordinates = valid_coordinates
        self.battery = battery
        self.temperature = temperature
