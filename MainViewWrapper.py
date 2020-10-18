from PyQt5 import QtWidgets

from MainView import MainView
from Space_Entity import Coordinate


class MainViewWrapper:

    def __init__(self):
        self.mv = MainView()
        self.MainWindow = QtWidgets.QMainWindow()
        self.map = []

    def show(self):
        self.mv.setupUi(self.MainWindow)
        self.__connectUi()
        self.MainWindow.show()

    def __connectUi(self):
        self.mv.Systems.currentRowChanged.connect(lambda: self.show_planets())
        self.mv.Planets.currentRowChanged.connect(lambda: self.show_space())
        self.mv.Planets.currentRowChanged.connect(lambda: self.show_orbit())
        self.mv.Planets.currentRowChanged.connect(lambda: self.show_land())

    @property
    def selected_system(self):
        return self.map[self.mv.Systems.currentRow()]

    @property
    def selected_planet(self):
        return self.selected_system.planets[self.mv.Planets.currentRow()]

    def __show_list(self, lst_widget, lst):
        lst_widget.clear()
        for ls in lst:
            item = QtWidgets.QListWidgetItem()
            item.setText(str(ls))
            lst_widget.addItem(item)

    def show_systems(self, systems):
        self.map = systems
        self.__show_list(self.mv.Systems, self.map)

    def show_planets(self):
        planets = self.map[self.mv.Systems.currentRow()].planets
        self.__show_list(self.mv.Planets, planets)

    def show_space(self):
        space = self.selected_system.get_sector_entities((self.selected_planet, Coordinate.Space))
        self.__show_list(self.mv.Space, space)

    def show_orbit(self):
        orbit = self.selected_system.get_sector_entities((self.selected_planet, Coordinate.Orbit))
        self.__show_list(self.mv.Orbit, orbit)

    def show_land(self):
        land = self.selected_system.get_sector_entities((self.selected_planet, Coordinate.Landed))
        self.__show_list(self.mv.Landed, land)
