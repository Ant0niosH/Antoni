#Antoni Handschuh

def jest_pierwsza(n):
    jest_p=True
    fpr l in range (2,n)
    if n % k == 0:
        jest_p = False
    return jest_P

import random
print("Tworzenie listy 200 lczb z zakresu od 2 do 1000")
tab = []
for j in range (200):
    liczba=random.randint(2,1000)
    tab.append(liczba)

print("Wylosowana listya: ")
print(tab)
input("Naciśnij enter...")

tab_pierw = []
for k in range(len(tab)):
    pierwsza=jest_pierwsza(tab[k])
    if pierwsza:
        tab_pierw.append(tab[k])

print("Liczby pierwsze z listy to: ")
print(tab_pierw)
print("Jest ich: ",len(tab_pierw))
input("Naciśnij enter")
