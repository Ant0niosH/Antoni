#Antoni Handschuh
#Random
#randint(a,b) <-- zwraca losową liczbę całkowitą N spełniającą nierówność a <= N <= b

import random
print ("Program losuje 20 liczb z podanego zakresu")
min = int(input("Podaj początek zakresu"))
max = int(input("Podaj koniec zakresu"))
if min >= max:
    print("Podałeś zły zakres")
else:
    suma=0
    for k in range (20):
        los=random.randint(min,max) #polecenie randint z modułu random losuje
        print(los)
        suma+=los
    średnia=suma/20
    print("średnia wylosowanych liczb: ", średnia)
input("Wciśnij enter")
