#obliczanie silni wersja pierwsza - za pomocą pętli for

print("Obliczanie silni")
n = int(input("Podaj liczbę naturalną: "))
if n < 0:
    print("Podałeś złą liczbe")
else:
    if n == 0:
        sil=1
    else:
        sil = 1
        for k in range(1,n+1):
            sil=sil*k
    print(n, "! = ", sil)
input("Naciśnij enter")
