from Ship import Ship
from Galaxy import Galaxy

g = Galaxy()
s = g.create_system()
ship = Ship()
s.enter_system(ship)
print("Yay!")
