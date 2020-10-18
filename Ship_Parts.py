from abc import ABC, abstractmethod

from Tick_Subjected import Tick_subjected


class AI(ABC):

    def __init__(self):
        self.ship = None

    @abstractmethod
    def begin_tick(self):
        pass

    @abstractmethod
    def end_tick(self):
        pass

    @abstractmethod
    def on_born(self):
        pass

    @abstractmethod
    def on_death(self):
        pass

    @abstractmethod
    def ai_pourpose(self):
        return "No-Action"


class Hull(ABC):

    def __init__(self, size, max_components, max_cargo, valid_coordinates, battery, temperature):
        self.size = size
        self.max_components = max_components
        self.max_cargo = max_cargo
        self.valid_coordinates = valid_coordinates
        self.battery = battery
        self.temperature = temperature
