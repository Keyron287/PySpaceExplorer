"""
La classe Ticker recupera tutti gli oggetti tick subjected e gli fa eseguire un tick
"""


class Ticker:
    """
    Fa eseguire un tick a tutte le entity della galassia
    """

    def __init__(self, galaxy):
        self.galaxy = galaxy

    def get_tickable(self):
        """Prende la lista di tick_subjected"""
        lst = []
        for s in self.galaxy.galaxy_map:
            lst += s.get_tick_active()
        return lst

    def execute_tick(self):
        """Esegue il tick di tutti gli oggetti tick_subjected"""
        lst = self.get_tickable()
        for t in lst:
            t.tick()
