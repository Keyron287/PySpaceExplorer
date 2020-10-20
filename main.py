"""
Main del programma
"""


import sys
from PyQt5 import QtWidgets
from Catalogs.Ai_catalog import PlaceHolder
from Data.Galaxy import Galaxy
from Catalogs.Hull_catalog import Whale
from Data.MainViewWrapper import MainViewWrapper
from Data.Ship import Ship
from Data.Ticker import Ticker
from Catalogs.Work_catalog import Builder


def starting_factory(ai):
    """
    Crea la prima costruzione del giocatore

    :param ai: La ai della prima factory
    :return: Nave modello Whale con factory e venti unità di metallo
    """
    f = Ship(ai, Whale())
    f.add_component(Builder())
    from Data.Resources import Box_of_metal
    for a in range(20):
        f.push_cargo(Box_of_metal())
    return f


app = QtWidgets.QApplication(sys.argv)

g = Galaxy()
s = g.create_system()
factory = starting_factory(PlaceHolder())
t = Ticker(g)
s.enter_system(factory)
ui = MainViewWrapper(t)
ui.show()
ui.show_systems(g.galaxy_map)

sys.exit(app.exec_())
