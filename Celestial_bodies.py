from random import randrange

import Space_Entity


class Celestial_body(Space_Entity.Space_Entity):

    def __init__(self, name, orbit=None):
        super().__init__(name)
        self.orbit = orbit


class Star(Celestial_body):

    def __init__(self):
        super().__init__(str(self.__class__.__name__))
        self.size = randrange(12000000, 1000000000)
        self.temperature = randrange(200, 200000)
        from Resources import Resources
        self.resources = {Resources.Light: randrange(1, 10)}


class Planet(Celestial_body):

    def __init__(self):
        super().__init__(str(self.__class__.__name__))
        self.size = randrange(200000, 10000000)
        self.temperature = randrange(-200, 2000)
        from Resources import Resources
        self.resources = {Resources.Metal: randrange(1, 1000000000), Resources.Radiation: randrange(1, 1000000)}


class Moon(Celestial_body):

    def __init__(self):
        super().__init__(str(self.__class__.__name__))
        self.size = randrange(2000, 100000)
        self.temperature = randrange(-200, 2000)
        from Resources import Resources
        self.resources = {Resources.Metal: randrange(1, 1000000000), Resources.Radiation: randrange(1, 1000000)}


class Asteroids(Celestial_body):

    def __init__(self):
        super().__init__(str(self.__class__.__name__))
        self.size = randrange(100, 1000)
        self.temperature = 0
        from Resources import Resources
        self.resources = {Resources.Metal: randrange(1, 1000000), Resources.Radiation: randrange(1, 1000)}




