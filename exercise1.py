import math

radius = float(input("vvedite radius \n"))
chisloPi = math.pi
dovginaCola = 2 * chisloPi * radius
ploshaCruga = chisloPi * math.pow(radius, 2)

print("Довжина кола дорівнює    ", dovginaCola)
print("Площа круга дорівнює   ", ploshaCruga)