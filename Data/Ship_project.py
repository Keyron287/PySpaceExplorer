"""
La classe ship_project crea è la "ricetta" che, caricata sul componente builder
spawna una nave spendendo il relativo costo
"""

from abc import ABC, abstractmethod


class Ship_project(ABC):

    @abstractmethod
    def build_energy(self) -> float:
        return 1

    @abstractmethod
    def needed_components(self) -> list:
        return []

    @abstractmethod
    def production_time(self) -> int:
        return 1

    @abstractmethod
    def produce_ship(self):
        pass
