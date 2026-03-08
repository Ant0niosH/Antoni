#Antoni Handschuh
#wykorzystanie listy append
import random
print('tworzenie listy (tablicy) 20 elementowej i operancje na niej program 20')
tab=[]
print('')
ile=int(input('Podaj ile liczb chcesz wylosować:  '))


for k in range(ile):
    los=random.randint(1,1000)
    tab.append(los)
    
dlug=len(tab)
print('tablica:  ',tab)
print('jej długość',dlug)
input('naciśnij ENTER')

print('Odwrócenie kolejności elementów w listy:')
tab.reverse()
print('tablica ofwrócona: ',tab)
input('naciśnij ENTER')


print('Największy element listy:')
print(max(tab))
print('Najmniejszy element listy')
print(min(tab))
print('Suma wszystkich liczb listy:')
print(sum(tab))
srednia=sum(tab)/len(tab)
print('średnia = %.2f' %srednia)
input('naciśnij ENTER')

print("Posorotwanie listy:")
tab.sort() #sortuje od najmniejszej wartości do najwiekszej
print("tablica posortowana: ", tab)
input("Naciśnij ENTER")

liczba=int(input("Podaj liczbe od 1 do 1000: "))
if liczba < 1 or liczba > 1000:
    print("Podałeś złą liczbę: ")
else:
    if liczba in tab:
        for k in range(len(tab)):
            if liczba == tab[k]:
                print("Ta liczba jest elementem listy o wskaźniku:", k)
        else:
            print("Ta liczba nie jest elementem tej listy")
input("Naciśnij enter")
