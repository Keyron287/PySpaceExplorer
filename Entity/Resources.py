from enum import Enum

from Entity.Space_Entity import Space_entity


class Resources(Enum):
    Light = 0
    Metal = 1
    Energy = 2
    Radiation = 3


class Resource_box(Space_entity):

    def __init__(self, base_resource: Resources):
        super().__init__(self.__class__.__name__, size=1)
        self.base = base_resource


class Box_of_metal(Resource_box):

    def __init__(self):
        super().__init__(Resources.Metal)


class Box_of_energy(Resource_box):

    def __init__(self):
        super().__init__(Resources.Energy)


class Box_of_radiation(Resource_box):

    def __init__(self):
        super().__init__(Resources.Radiation)


class Box_of_light(Resource_box):

    def __init__(self):
        super().__init__(Resources.Light)
