#kubus
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

