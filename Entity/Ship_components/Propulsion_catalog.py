from typing import List

from Entity.Component import Component
from Entity.Space_Entity import Space_entity
from Space_System import Space_system
from Tick_Subjected import Tick_action


class Flyer(Component):

    def get_size(self) -> int:
        return 2

    def get_energy_usage(self) -> float:
        return 5

    def use(self, *param) -> List[Tick_action]:
        pass
