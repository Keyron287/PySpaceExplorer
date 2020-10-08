from Entity.Ship_Parts import Hull
from Entity.Space_Entity import Coordinate


class Ant(Hull):

    def __init__(self):
        super().__init__(1, 1, 2, (Coordinate.Landed, Coordinate.Orbit, Coordinate.Space), 200, 0)


class Wasp(Hull):

    def __init__(self):
        super().__init__(1, 2, 1, (Coordinate.Landed, Coordinate.Orbit, Coordinate.Space), 20, 0)


class Rhino(Hull):

    def __init__(self):
        super().__init__(1, 5, 5, (Coordinate.Landed, Coordinate.Orbit, Coordinate.Space), 100, 0)


class Whale(Hull):

    def __init__(self):
        super().__init__(10, 10, 20, (Coordinate.Orbit, Coordinate.Space), 200, 0)


class Titan(Hull):

    def __init__(self):
        super().__init__(50, 15, 100, (Coordinate.Orbit, Coordinate.Space), 200, 0)


class Atlas(Hull):

    def __init__(self):
        super().__init__(100, 20, 1000, (Coordinate.Space,), 1000, 0)


