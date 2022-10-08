import math

diametr = float(input("Введіть діаметр \n"))
radius = diametr / 2
chisloPi = math.pi
ploshaCruga = chisloPi * math.pow(radius, 2)

print("Площа круга дорівнює   ", ploshaCruga)