"""
Component è la classe padre che definisce tutta la strumentazione della
nave
"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import List

from Data.Tick_Subjected import Tick_action


class Category(Enum):
    """Le categorie dei componenti"""
    Energy = 0
    Propulsion = 1
    Sensor = 2
    Work = 3


class Component(ABC):
    """Componenti della nave"""

    def __init__(self):
        self.parent = None

    @abstractmethod
    def get_category(self):
        """
        La categoria del componente
        :return: Restituisce la categoria del compoente
        """
        pass

    @abstractmethod
    def get_size(self) -> int:
        """
        Il size del componente
        :return: Restituisce il size del compoente
        """
        return 1

    @abstractmethod
    def get_energy_usage(self) -> float:
        """
        L'utilizzo dell'energia del componente
        :return: Restituisce l'energia utilizzata dal compoente
        """
        return 0.75

    @abstractmethod
    def get_duration(self) -> int:
        """
        La durata dell'operazione fatta dal componente
        :return: Restitusce la durata dell'uso del componente
        """
        return 0

    @abstractmethod
    def use(self, *param) -> List[Tick_action]:
        """
        :param param: Parametri necessari per l'utilizzo del componente
        :return: La tick action relativa al compoente
        """
        pass


class Cluster_component(Component):
    """Struttura di componenti utilizzabili in parallelo"""

    def __init__(self, cls, qnt):
        super().__init__()
        self.childs: List[Component] = []
        for a in range(qnt):
            self.childs.append(cls())

    def get_category(self):
        return self.childs[0].get_category()

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
