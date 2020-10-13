from enum import Enum

from Space_Entity import Resource_box


class Resources(Enum):
    Light = 0
    Metal = 1
    Energy = 2
    Radiation = 3


class Box_of_metal(Resource_box):

    def __init__(self):
        super().__init__(Resources.Metal)


class Box_of_energy(Entity.Space_Entity.Resource_box):

    def __init__(self):
        super().__init__(Resources.Energy)


class Box_of_radiation(Entity.Space_Entity.Resource_box):

    def __init__(self):
        super().__init__(Resources.Radiation)


class Box_of_light(Entity.Space_Entity.Resource_box):

    def __init__(self):
        super().__init__(Resources.Light)
