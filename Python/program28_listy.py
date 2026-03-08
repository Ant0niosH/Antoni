#kubus
#wykorzystanie listy append
import random
print('tworzenie listy (tablicy) 20 elementowej i operancje na niej program 20')
tab=[]
print('tablica:  ',tab)
print('jej długość',dlug)
input('naciśnij ENTER')

for k in range(20):
    los=random.randint(1,1000)
    tab.append(los)
dlug=len(tab)
print('tablica:  ',tab)
print('jej długość',dlug)
input('naciśnij ENTER')
for k in range (len(tab)):
    print('k=',k,' tab[k] ='tab[k])
input('naciśnij ENTER')

print('Pobranie i usunięcie z listy elem. o indeksie 4')
elem=tab.pop(4)
print('element usunięty: ',elem)
dlug = len(tab)
print('tablica: ',tab)
print('jej długość: ',dlug)
input('naciśnij ENTER')

print('wstawianie na koniec listy wylosowanego elementu')
elem=random.randint(1,1000)
print('element wylosowany: ',elem)
tab.append(elem)
for k in range(dlug):
    los=random.randint(1,1000)
    tablica[k]=los
print(tablica)
dlug=len(tablica)
print('długość listy',dlug)
input('nacisnij ENTER')
n=int(input('który element listy chcesz zobaczyć: '))
if n> 20 or n<1:
    print('zła liczba')
else:
    print('element nr ',n,' listy to: ',tablica[n-1])
input('naciśnij ENTER')
