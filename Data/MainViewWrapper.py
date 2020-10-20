"""
Contiene il wrapper dell'interfaccia grafica
"""

from PyQt5 import QtWidgets

from Data.MainView import Ui_MainWindow
from Data.Space_Entity import Coordinate


class MainViewWrapper:

    def __init__(self, ticker):
        self.mv = Ui_MainWindow()
        self.MainWindow = QtWidgets.QMainWindow()
        self.map = []
        self.ticker = ticker

    def show(self):
        """Visualizza l'interfaccia"""
        self.mv.setupUi(self.MainWindow)
        self.__connectUi()
        self.MainWindow.show()

    def __connectUi(self):
        """Genera le connessioni per le interazioni con l'interfaccia"""
        self.mv.Systems.currentRowChanged.connect(lambda: self.show_planets())
        self.mv.Planets.currentRowChanged.connect(lambda: self.show_space())
        self.mv.Planets.currentRowChanged.connect(lambda: self.show_orbit())
        self.mv.Planets.currentRowChanged.connect(lambda: self.show_land())
        self.mv.next_tick.clicked.connect(lambda: self.tick())

    @property
    def selected_system(self):
        return self.map[self.mv.Systems.currentRow()]

    @property
    def selected_planet(self):
        return self.selected_system.planets[self.mv.Planets.currentRow()]

    def __show_list(self, lst_widget, lst):
        """Inserisce la lista nel lst_widget"""
        lst_widget.clear()
        for ls in lst:
            item = QtWidgets.QListWidgetItem()
            item.setText(str(ls))
            lst_widget.addItem(item)

    def tick(self):
        """Esegue esegue un tick ed aggiorna l'interfaccia"""
        last_system = self.mv.Systems.currentRow()
        last_planet = self.mv.Planets.currentRow()
        self.ticker.execute_tick()
        self.show_systems()
        self.mv.Systems.setCurrentRow(last_system)
        self.show_planets()
        self.mv.Planets.setCurrentRow(last_planet)
        self.show_space()
        self.show_orbit()
        self.show_land()

    def show_systems(self, systems=None):
        """Aggiorna la lista dei sistemi"""
        self.map = systems or self.map
        self.__show_list(self.mv.Systems, self.map)

    def show_planets(self):
        """Aggiorna la lista dei pianeti"""
        planets = self.map[self.mv.Systems.currentRow()].planets
        self.__show_list(self.mv.Planets, planets)

    def show_space(self):
        """Aggiorna la lista delle unità nello spazio"""
        space = self.selected_system.get_sector_entities((self.selected_planet, Coordinate.Space))
        self.__show_list(self.mv.Space, space)

    def show_orbit(self):
        """Aggiorna la lista delle unità in orbita"""
        orbit = self.selected_system.get_sector_entities((self.selected_planet, Coordinate.Orbit))
        self.__show_list(self.mv.Orbit, orbit)

    def show_land(self):
        """Aggiorna la lista delle unità a terra"""
        land = self.selected_system.get_sector_entities((self.selected_planet, Coordinate.Landed))
        self.__show_list(self.mv.Landed, land)
