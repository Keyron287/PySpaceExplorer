from PyQt5 import QtWidgets
import sys
from Hull_catalog import Ant
from MainView import MainView
from MainViewWrapper import MainViewWrapper
from Ship import Ship
from Galaxy import Galaxy
from Ship_Parts import AI
from Ticker import Ticker

app = QtWidgets.QApplication(sys.argv)

g = Galaxy()
s = g.create_system()
ship = Ship(AI(), Ant())
t = Ticker(g)
t.execute_tick()
s.enter_system(ship)
ui = MainViewWrapper()
ui.show()
ui.show_systems(g.galaxy_map)

sys.exit(app.exec_())
