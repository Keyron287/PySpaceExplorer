from PyQt5 import QtWidgets
import sys

from Ai_catalog import Lift
from Hull_catalog import Ant, Wasp
from MainView import MainView
from MainViewWrapper import MainViewWrapper
from Propulsion_catalog import Flyer
from Ship import Ship
from Galaxy import Galaxy
from Ship_Parts import AI
from Ticker import Ticker

app = QtWidgets.QApplication(sys.argv)

g = Galaxy()
s = g.create_system()
ship = Ship(Lift(), Wasp())
ship.add_component(Flyer())
t = Ticker(g)
s.enter_system(ship)
ui = MainViewWrapper()
ui.show()
ui.show_systems(g.galaxy_map)
t.execute_tick()

sys.exit(app.exec_())
