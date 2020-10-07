from typing import List

from Entity.Space_Entity import Space_entity


class Space_system:

    def __init__(self):
        self.map = {
            # planet : [[landed], [orbit], [space]]
        }
        self.connections: List[Space_system] = []
        self.__generate()

    def __generate(self):
        pass

    def enter_system(self, entity):
        pass

    def exit_system(self, entity):
        pass
