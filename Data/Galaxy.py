"""
Contiene la classe Galaxy, quella che contiene ogni componente nel gioco
"""

from random import randrange
from typing import List

from Data import Space_System


class Galaxy:
    """
    Contiene tutti i sistemi del gioco, galaxy_map è la lista dei sistemi del gioco
    """
    galaxy_map: List = []

    def create_system(self):
        """
        Genera un sistema e le relative connessioni
        :return: Il sistema generato
        """
        n = Space_System.Space_system()
        self.galaxy_map.append(n)
        self.generate_system_connections(n)
        return n

    def generate_system_connections(self, start_system):
        """
        Crea le connessioni tra sistemi
        :param start_system: Il sistema da dove si creano le connessioni
        """
        connections = min(randrange(1, 3), 3-len(start_system.connections))
        for a in range(connections):
            n = Space_System.Space_system()
            self.galaxy_map.append(n)
            start_system.connections.append(n)
            n.connections.append(start_system)
