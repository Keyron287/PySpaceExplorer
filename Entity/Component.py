from abc import ABC, abstractmethod
from Tick_Subjected import Tick_action


class Component(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_size(self) -> int:
        return 1

    @abstractmethod
    def get_energy_usage(self) -> float:
        return 0.75

    @abstractmethod
    def use(self, *param) -> Tick_action:
        pass
