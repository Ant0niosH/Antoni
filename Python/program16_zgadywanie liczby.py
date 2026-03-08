#Antoni Handschuh
#Random
#randint(a,b) <-- zwraca losową liczbę całkowitą N spełniającą nierówność a <= N <= b

import random
los=random.randint(0,1000)
liczba = -1
while (liczba != los):
    liczba = int(input("Podaj liczbę w zakresie 1 - 1000 "))
    if (liczba > los):
        print("Za duza")
    elif (liczba < los):
        print("Za mała")
else:
    print("Dobra liczba")
input("Naciśnij enter")
