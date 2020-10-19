import sys
from PyQt5 import QtWidgets
from Catalogs.Ai_catalog import PlaceHolder
from Galaxy import Galaxy
from Catalogs.Hull_catalog import Whale
from MainViewWrapper import MainViewWrapper
from Ship import Ship
from Ticker import Ticker
from Catalogs.Work_catalog import Builder


def starting_factory():
    f = Ship(PlaceHolder(), Whale())
    f.add_component(Builder())
    from Resources import Box_of_metal
    for a in range(20):
        f.push_cargo(Box_of_metal())
    return f


app = QtWidgets.QApplication(sys.argv)

g = Galaxy()
s = g.create_system()
factory = starting_factory()
t = Ticker(g)
s.enter_system(factory)
ui = MainViewWrapper(t)
ui.show()
ui.show_systems(g.galaxy_map)

sys.exit(app.exec_())
