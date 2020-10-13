from random import randrange
from typing import List

import Space_System


class Galaxy:

    galaxy_map: List = []

    def create_system(self):
        n = Space_System.Space_system()
        self.galaxy_map.append(n)
        self.generate_system_connections(n)
        return n

    def generate_system_connections(self, start_system):
        connections = min(randrange(0, 3), 3-len(start_system.connections))
        for a in range(connections):
            n = Space_System.Space_system()
            self.galaxy_map.append(n)
            start_system.connections.append(n)
            n.connections.append(start_system)
