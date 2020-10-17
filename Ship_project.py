from abc import ABC


class Ship_project(ABC):

    def build_energy(self) -> float:
        return 1

    def needed_components(self) -> list:
        return []

    def production_time(self) -> int:
        return 1

    def produce_ship(self):
        pass
