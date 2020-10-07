from abc import ABC, abstractmethod

from typing import List

from Tick_Subjected import Tick_action


class Component(ABC):

    @abstractmethod
    def get_size(self) -> int:
        return 1

    @abstractmethod
    def get_energy_usage(self) -> float:
        return 0.75

    @abstractmethod
    def use(self, *param) -> List[Tick_action]:
        pass


class Cluster_component(Component):

    def __init__(self, *components: Component):
        self.childs: List[Component] = []
        for a in components:
            self.childs.append(a)

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

    def use(self, *param) -> List[Tick_action]:
        pass
