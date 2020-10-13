from abc import ABC


class Ship_project(ABC):

    def build_energy(self):
        return 1

    def needed_components(self):
        return []

    def produce_ship(self):
        pass
