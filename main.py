import sys

from PyQt5 import QtWidgets

from Ai_catalog import Lift
from Galaxy import Galaxy
from Hull_catalog import Wasp
from MainViewWrapper import MainViewWrapper
from Propulsion_catalog import Flyer
from Ship import Ship
from Ticker import Ticker

app = QtWidgets.QApplication(sys.argv)

g = Galaxy()
s = g.create_system()
factory = Ship(Lift(), Wasp())
factory.add_component(Flyer())
t = Ticker(g)
s.enter_system(factory)
ui = MainViewWrapper(t)
ui.show()
ui.show_systems(g.galaxy_map)

sys.exit(app.exec_())
