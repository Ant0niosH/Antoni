#Antoni Handschuh
#zadanie 14
#program prosi o podawania liczb całkowitych tak długo
#dopóki nie podamy liczby ZERO
#nastepnie podaje ilosc podanych liczb (bez zera)
#oraz ich sume

suma = 0
ile = 0
while True:
    liczba=int(input("Podaj liczbę całkowitą: "))
    suma += liczba
    if liczba != 0:
        print("Prawidłowa liczba")
    else:
        break
    ile+=1
print("Wprowadziłeś", ile, "liczb")
print("Ich suma wynosi: ", suma)
print("Naciśnij enter")
