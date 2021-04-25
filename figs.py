from tables import *

color = "#4c0618"

a = Animate_number([399,400],855,put_numbers=False,size=1000,step=0.01, color=color)
a.save(dir="frames/1")

a = Animate_mod(2,[3,100],put_numbers=False,size=500, color=color)
a.save(dir="frames/2")

a = Table(41,84,put_numbers=False,size=500, color=color, name="rectangles")
a.save(dir="frames/3")

a = Table(28,378,put_numbers=False,size=500, color=color)
a.save(dir="frames/4")
