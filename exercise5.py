import math

katetA = float(input("Введіть перший катет\n"))
katetB = float(input("Введіть другий катет\n"))

gipotenuza = math.hypot(katetA, katetB)

print("Гіпотенуза дорівнює   ", gipotenuza)