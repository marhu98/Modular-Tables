from tables import *

a = Animate_number([399,400],855,put_numbers=False,size=1000,step=0.01, color="#0d6d4d",)
a.save(dir="frames/1")

a = Animate_mod(2,[3,100],put_numbers=False,size=500, color="#0d6d4d")
a.save(dir="frames/2")

a = Table(41,84,put_numbers=False,size=500, color="#0d6d4d", name="rectangles")
a.save(dir="frames/3")
