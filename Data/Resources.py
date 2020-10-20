from enum import Enum

from Data.Space_Entity import Space_Entity


class Resources(Enum):
    """Elenco dei tipi di risorse"""
    Light = 0
    Metal = 1
    Energy = 2
    Radiation = 3


class Resource_box(Space_Entity):
    """Unità materiale di risorsa, sotto forma di Box. Derivata da Space_Entity"""
    def __init__(self, base_resource: Resources):
        super().__init__(size=1)
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
