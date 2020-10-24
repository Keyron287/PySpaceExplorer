"""
Questo modulo contiene la classe Tick_subjected che rappresenta le unità che cambiano
col passare del tempo
"""

from abc import ABC, abstractmethod
from typing import List, final


class Tick_action(ABC):
    """
    Classe che rappresenta le azioni gestite da tick_subjected
    """

    @abstractmethod
    def msg(self) -> str:
        """Il messaggio che visualizza la tick_action"""
        pass

    @abstractmethod
    def execute(self):
        """L'azione eseguida dalla classe Tick_action"""
        pass


class Delay(Tick_action):
    """Classe derivata da tick action che gestisce il delay delle azioni,
    funziona da placeholder"""

    def __init__(self, msg):
        self.msg = msg

    def msg(self) -> str:
        return self.msg

    def execute(self):
        pass


class Tick_subjected(ABC):
    """
    Tick_subjected gestisce le azioni della classe, questa contiene una
    lista di Tick_actions ne viene eseguita una per tick.
    """

    def __init__(self):
        self.actions = []
        self.current_action = None

    def add_action(self, action: List[Tick_action], duration: int = 1):
        """Aggiunge una azione alla lista"""
        for a in range(duration - 1):
            self.actions.append([Delay(action[0].msg())])
        self.actions.append(action)

    def rem_action(self, action: Tick_action):
        pass

    def begin_tick(self):
        """Esegue operazioni prima del tick"""
        pass

    # Final impedisce che un metodo sia sovrascritto
    @final
    def tick(self):
        """Viene estratta la prima azione della lista ed eseguita"""
        self.begin_tick()  # Esegue begin tick, prima di eseguire l'azione
        if len(self.actions) > 0:
            action = self.actions.pop(0)
            for a in action:  # Esegue tutte le azioni in cima alla lista
                try:
                    self.current_action = a
                    a.execute()
                except Exception as err:
                    print("Error:", err)
            self.end_tick()

    def end_tick(self):
        """Effettua operazioni dopo il tick"""
        pass
