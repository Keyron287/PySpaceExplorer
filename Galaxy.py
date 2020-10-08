from random import randrange
from typing import List

from Space_System import Space_system


class Galaxy:

    galaxy_map: List[Space_system] = None

    def generate_system_connections(self, start_system: Space_system):
        connections = min(randrange(0, 3), 3-len(start_system.connections))
        for a in range(connections):
            n = Space_system()
            start_system.connections.append(n)
            n.connections.append(start_system)
