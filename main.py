from Hull_catalog import Ant
from Ship import Ship
from Galaxy import Galaxy
from Ship_Parts import AI

g = Galaxy()
s = g.create_system()
ship = Ship(AI(), Ant())
s.enter_system(ship)
print("Yay!")
