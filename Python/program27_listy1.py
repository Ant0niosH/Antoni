import random
print("Tworzenie listy (tablicy) 20 elementowej i operacje na niej program 2")
tablica=list(range(20))#zakres 20
print(tablica)
dlug=len(tablica)
print("Długośc listy wynosi: ",dlug)
input("Naciśnij enter")
print()
print("Zerowanie listy")
for k in range(dlug):
    tablica[k] = 0
print(tablica)
dlug=len(tablica)
print("długość list: ", dlug)
print("Naciśnij enter")
print()
print("losowanei tablicy")
for k in range(dlug):
    los=random.randint(1,1000)
    tablica[k]=los
print(tablica)
dlug=len(tablica)
print("Długośc listy: ", dlug)
input("Naciśnij enter")
n=int(input("Który element liczby chcesz zobaczyć: "))
if n > 20 or n<1:
    print("Zła liczba")
else:
    print("Element nr", n, "listy to: ", tablica[n-1])
input("Naciśnij enter")
