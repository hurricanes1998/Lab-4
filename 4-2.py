nomer_mesta = None

while not nomer_mesta:
        nomer_mesta = input("Место: ")

if int(nomer_mesta) in range(37, 55):
        print("Место боковое")

if int(nomer_mesta) % 2 == 0:
        print("Место верхнее")

else:
        print("Место нижнее")

import random