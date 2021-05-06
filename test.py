v = 'anna'
v = 'i' + v[1:]
print(v)

import math


nosaukums = input('Ievadi preces nosaukumu ==> ')
cena = float(input('Ievadi preces cenu ==> '))
skaits = int(input('Ievadi skaiti ==> '))
summa = round(cena * skaits, 2)

print(nosaukums)
print(cena)
print(summa)

print('Prece:', nosaukums)
print('Prece: ' + nosaukums)
print('Summa: ' + str(summa))

print("Cena: ", end = "")
print(cena)

print(cena, skaits, summa, sep = "\n")

print(math.sqrt(cena))

print()
print(type(cena))

print('make more changes')
