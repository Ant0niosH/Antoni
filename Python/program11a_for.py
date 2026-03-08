#Antoni Handschuh
#program pyta o liczbę początkową oraz o wartość różnicy i
#wypisuje tylke kolejnych liczb poczawszy od liczby początkowej
#różniąca się o wartość różnicy, ile podamy

print("Wypisywanie 20 liczb")
print
start=int(input("Podaj liczbę pocztkową: "))
róznica=int(input("Podaj różnicę: "))
powtorzenia=int(input("Podaj liczbę powtórzeń: "))
liczba = start
for j in range(powtorzenia):
    print(liczba)
    liczba+=róznica
    if liczba > 1000:
        break
input("Naciśnij enter")
