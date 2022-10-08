import math

katetA = float(input("Введіть перший катет\n"))
gipotenuza = float(input("Введіть Гіпотенузу\n"))

katetB = math.sqrt(math.pow(gipotenuza, 2) - math.pow(katetA, 2) )

print("Другий катет дорівнює  ",  katetB)