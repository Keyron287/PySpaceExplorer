from enum import Enum
from random import randrange
from Entity.Space_Entity import Space_entity


class Celestial_body(Space_entity):

    def __init__(self, name, orbit=None):
        super().__init__(name)
        self.orbit = orbit


class Star(Celestial_body):

    def __init__(self):
        super().__init__(str(self.__class__.__name__))
        self.size = randrange(12000000, 1000000000)
        self.temperature = randrange(200, 200000)
        self.resources = {Resources.Light: randrange(1, 10)}


class Planet(Celestial_body):

    def __init__(self):
        super().__init__(str(self.__class__.__name__))
        self.size = randrange(200000, 10000000)
        self.temperature = randrange(-200, 2000)
        self.resources = {Resources.Metal: randrange(1, 1000000000), Resources.Radiation: randrange(1, 1000000)}


class Moon(Celestial_body):

    def __init__(self):
        super().__init__(str(self.__class__.__name__))
        self.size = randrange(2000, 100000)
        self.temperature = randrange(-200, 2000)
        self.resources = {Resources.Metal: randrange(1, 1000000000), Resources.Radiation: randrange(1, 1000000)}


class Asteroids(Celestial_body):

    def __init__(self):
        super().__init__(str(self.__class__.__name__))
        self.size = randrange(100, 1000)
        self.temperature = 0
        self.resources = {Resources.Metal: randrange(1, 1000000), Resources.Radiation: randrange(1, 1000)}




