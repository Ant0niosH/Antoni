#kubus
#wykorzystanie listy append
import random
print('tworzenie listy (tablicy) 20 elementowej i operancje na niej program 20')
tab=[]

for k in range(20):
    los=random.randint(1,1000)
    tab.append(los)
    
dlug=len(tab)
print('tablica:  ',tab)
print('jej długość',dlug)
input('naciśnij ENTER')
print('obliczanie sumy, średniej liczb z listy')
print(' szukanie najmniejszego i największego elementu')
suma=0
minimum=tab[0]
maksimum=tab[0]
for k in range (len(tab)):
    suma+=tab[k]
    if minimum > tab[k]:
        minimum=tab[k]
    if maksimum <tab[k]:
        maksimum=tab[k]
srednia=suma/len(tab)
print('suma= ',suma)
print('średnia = %.2f' %srednia)
print('min = ',minimum,' , max= ',maksimum)
input('naciśnij ENTER')

