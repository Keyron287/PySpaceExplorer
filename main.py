from Hull_catalog import Ant
from Ship import Ship
from Galaxy import Galaxy
from Ship_Parts import AI
from Ticker import Ticker

g = Galaxy()
s = g.create_system()
ship = Ship(AI(), Ant())
t = Ticker(g)
t.execute_tick()
s.enter_system(ship)
print("Yay!")
