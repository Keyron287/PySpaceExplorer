from typing import List

from Component import Category
from Propulsion_catalog import Flyer
from Ship_Parts import AI
from Space_Entity import Coordinate
from Work_catalog import Mover


class PlaceHolder(AI):

    def begin_tick(self):
        pass

    def end_tick(self):
        pass

    def on_born(self):
        pass

    def on_death(self):
        pass

    def ai_pourpose(self):
        return "Place holder"


class Lift(AI):

    def __init__(self):
        super().__init__()
        self.ascend = True

    def begin_tick(self):
        if self.ship.position[1] == Coordinate.Space:
            self.ascend = False
        if self.ship.position[1] == Coordinate.Landed:
            self.ascend = True

        if self.ship.has_component(Flyer):
            move: List[Flyer] = self.ship.get_components(Category.Propulsion, Flyer)
            self.ship.add_action(move[0].use(ascend=self.ascend, away=None))
        else:
            raise Exception("Cannot move without Flyer")

    def end_tick(self):
        pass

    def on_born(self):
        pass

    def on_death(self):
        pass

    def ai_pourpose(self):
        return "Lift"
