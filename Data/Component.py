from abc import ABC, abstractmethod
from enum import Enum
from typing import List

from Data.Tick_Subjected import Tick_action


class Category(Enum):
    Energy = 0
    Propulsion = 1
    Sensor = 2
    Work = 3


class Component(ABC):

    def __init__(self):
        self.parent = None

    @abstractmethod
    def get_category(self):
        pass

    @abstractmethod
    def get_size(self) -> int:
        return 1

    @abstractmethod
    def get_energy_usage(self) -> float:
        return 0.75

    @abstractmethod
    def get_duration(self) -> int:
        return 0

    @abstractmethod
    def use(self, *param) -> List[Tick_action]:
        pass


class Cluster_component(Component):

    def __init__(self, cls, qnt):
        super().__init__()
        self.childs: List[Component] = []
        for a in range(qnt):
            self.childs.append(cls())

    def get_size(self) -> int:
        r = 1
        for a in self.childs:
            r += a.get_size()
        return r

    def get_energy_usage(self) -> float:
        r = 1
        for a in self.childs:
            r += a.get_size()
        return r

    def get_duration(self) -> int:
        mx = 0
        for a in self.childs:
            mx = max(mx, a.get_duration())
        return mx

    def use(self, *param) -> List[Tick_action]:
        r = []
        for a in self.childs:
            r += a.use(param)
        return r
