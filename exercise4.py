import math

PloshaCruga = float(input("Введіть площу круга\n"))
chisloPi = math.pi

radius = math.sqrt(PloshaCruga / chisloPi)
diametr = 2 * radius
print("Діаметр круга дорівнює   ", diametr)