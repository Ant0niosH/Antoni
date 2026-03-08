#Antoni Handschuh
#wlasne zadanie

haslo = ""
bledneHaslo = 0
while haslo!="ABC":
    haslo == input("Podaj hasło: ")
    if haslo =="ABC":
        print("Prawidłowe hasło")
    else:
        print("Złe hasło, spróbuj raz jeszcze")
        bledneHaslo += 1
        if(bledneHaslo == 3):
            print("Przekroczyłeś liczbę prób.")
            break
    
