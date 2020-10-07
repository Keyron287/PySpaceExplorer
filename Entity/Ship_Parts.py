from abc import ABC

from Tick_Subjected import Tick_subjected


class AI(ABC, Tick_subjected):
    pass


class Hull(ABC):

    def __init__(self, size, max_components, max_cargo, valid_coordinates, battery, temperature):
        self.size = size
        self.max_components = max_components
        self.max_cargo = max_cargo
        self.valid_coordinates = valid_coordinates
        self.battery = battery
        self.temperature = temperature
