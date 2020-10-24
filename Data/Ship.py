"""
Classe Ship
"""

from typing import final, List

from Catalogs.Ai_catalog import AI
from Catalogs.Hull_catalog import Hull
from Data.Component import Component, Category
from Data.Space_Entity import Space_Entity


class Battery_Exception(Exception):
    def __init__(self, message):
        super().__init__(message)


# final non fa estendere la classe
@final
class Ship(Space_Entity):

    def __init__(self, ai, hull):
        self._ai: AI = ai
        self._ai.ship = self
        self._hull: Hull = hull
        self._battery: float = self.hull.battery
        self._components: List[Component] = []
        self._cargo: List[Space_Entity] = []
        super().__init__(size=self._hull.size, temperature=self._hull.temperature,
                         accessible_coordinates=self._hull.valid_coordinates)

    @property
    def current_action_msg(self):
        """Restituisce l'azione corrente della nave, restituisce nothing se non ci sono azioni"""
        try:
            return self.current_action.msg()
        except AttributeError:
            return "Nothing"

    def __repr__(self):
        return self._hull.__class__.__name__ + "(" + self.ai.ai_pourpose() + ")[" + self.current_action_msg + "]"

    @property
    def ai(self):
        return self._ai

    @ai.setter
    def ai(self, value):
        self._ai = value

    @property
    def hull(self):
        return self._hull

    @hull.setter
    def hull(self, value):
        self._hull = value

    @property
    def battery(self):
        return self._battery, self._hull.battery

    @property
    def cargo(self):
        return self._cargo

    @property
    def components(self):
        return self._components

    def get_components(self, cat: Category, cls=None):
        """
        Fornisce la lista di componenti filtrati per categoria e per classe(otp)
        :param cat: La categoria del componente
        :param cls: La classe dei componenti richiesti
        :return: Restituisce una lista filtrata di componenti della nave
        """
        if cls is None:
            return list(filter(lambda x: x.get_category() == cat, self._components))
        else:
            return list(filter(lambda x: x.get_category() == cat and isinstance(x, cls), self._components))

    def has_component(self, cls):
        """
        Confronta se la nave ha il determinato componente
        :param cls: la classe del componente richiesto
        :return: Restituisce True se la nave possiede il componente richiesto
        """
        for a in self._components:
            if isinstance(a, cls):
                return True
        return False

    def add_component(self, component):
        """
        Aggiunge il componente alla nave, solleva un'eccezione se non c'è spazio
        per aggiungerlo
        :param component: Il componente da aggiungere
        """
        if len(self._components) + component.get_size() <= self._hull.max_components:
            component.parent = self
            self._components.append(component)
        else:
            raise Exception("Not enough space for component")

    def rem_component(self, component):
        """Rimuove il componente"""
        self._components.remove(component)

    def push_cargo(self, cargo: Space_Entity):
        """
        Carica una space entity nello spazio di cargo della nave, solleva un errore
        se non c'è spazio. Il caroco è una coda LIFO (Last in, first out)
        :param cargo: l'oggetto da stipare
        """
        if len(self._components) + cargo.size < self._hull.max_cargo:
            self.cargo.append(cargo)
        else:
            raise Exception("Cargo is full!")

    def pop_cargo(self):
        """Restituisce l'ultimo elemento del cargo"""
        return self.cargo.pop(-1)

    def get_cargo(self, needed: list):
        """
        Restituisce la lista di materiali nel cargo, necessaria per la produzione
        :param needed: La lista di materiali necessari
        """
        # TODO Da rivedere nel caso
        if set(needed).issubset(set(self._cargo)):
            self._cargo = [x for x in self._cargo if x not in needed]
            return needed
        else:
            raise Exception("Not enough materials")

    def use_battery(self, quantity):
        """
        Usa la batteria della nave, solleva un eccezione se non ha abbastanza energia
        :param quantity: La quantità di energia consumata
        """
        if quantity < self._battery:
            raise Battery_Exception("Insufficient Energy")
        else:
            self._battery -= quantity

    def charge_battery(self, quantity):
        """Ricarica la batteria di quantity"""
        self._battery = min(self._hull.battery, self._battery + quantity)

    def fly(self, ascend=None, away=None):
        """Fa muovere la nave nello spazio, se ha un componente flyer"""
        self.system.flight(self, ascend, away)

    def begin_tick(self):
        self._ai.begin_tick()

    def end_tick(self):
        self._ai.end_tick()
