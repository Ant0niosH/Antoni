def silnia(x):
    if x == 0:
        return 1
    else:
        sil = 1
        return x*ilnia(x-1) #funkca wywołuje samą siebie z parametrem o 1 mniejszym
print("Obliczanie silni ver 2 z funkcja ITERACYJNIE program 25")
n=int(input("Podaj liczbę naturalną: "))
if n < 0:
    print("Podałeś liczbę ujemna")
else:
    wynik=silnia(n)
    print(n,"! = ",wynik)

input("Naciśnij enter")
