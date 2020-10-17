
class Ticker:

    def __init__(self, galaxy):
        self.galaxy = galaxy

    def get_tickable(self):
        lst = []
        for s in self.galaxy.galaxy_map:
            lst += s.get_tick_active()
        return lst

    def execute_tick(self):
        lst = self.get_tickable()
        for t in lst:
            t.tick()
