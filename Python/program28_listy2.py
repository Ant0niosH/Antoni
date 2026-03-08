import random
print("Tworzenie listy dynamicznej i operacje nan iej program 28")
tab =[]
dlug = len(tab)
print("Tablica: ", tab)
print("jej długość: ", dlug)
input("Naciśnij enter")

for k in range(20):
    los=random.randint(1,1000)
    tab.append(los)#dopisywanie na końcu listy wylosowanego elemnetu
dlug = len(tab)
print("Tablica: ", tab)
print("jej długość: ", dlug)
input("Naciśnij enter")
for k in range (len(tab)):
    print("k ", k, " tab[k] =",tab[k])
input("Nacijśnij enter")

print("Usuwanie z listy elementy o indeksie 2")
del(tab[2])#usuwanie z listy elementu
dlug=len(tab)
print("Tablica: ", tab)
print("jej długość: ", dlug)
input("Naciśnij enter")

print("Pobranie i usuniecie z listy elem. o indeksie 4")
elem=tab.pop(4) #usuwanie z listy elementu sposób drugi
print("element usunięty: ",elem)
dlug=len(tab)
print("Tablica: ", tab)
print("jej długość: ", dlug)
input("Naciśnij enter")

print("Wstawianie na koniec listy wylosowanego elementu: ")
elem=random.randint(1,1000)
print("element wylosowany ", elem)
tab.append(elem)
dlug=len(tab)
print("Tablica: ", tab)
print("jej długość: ", dlug)
input("Naciśnij enter")
