from PyQt5 import QtWidgets
import sys

from Ai_catalog import Lift
from Hull_catalog import Ant, Wasp
from MainViewWrapper import MainViewWrapper
from Propulsion_catalog import Flyer
from Ship import Ship
from Galaxy import Galaxy
from Ticker import Ticker

app = QtWidgets.QApplication(sys.argv)

g = Galaxy()
s = g.create_system()
ship = Ship(Lift(), Wasp())
ship.add_component(Flyer())
t = Ticker(g)
s.enter_system(ship)
ui = MainViewWrapper(t)
ui.show()
ui.show_systems(g.galaxy_map)

sys.exit(app.exec_())
