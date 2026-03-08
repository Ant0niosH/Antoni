#Antoni Handschuh
#zadanei 12
#petla while
print("pętla WHILE wersja 1")
haslo = ""
while haslo != "ABC": #symbol != oznacza "nie równa się"
    haslo = input("Podaj haslo: ")
    if haslo =="ABC":
        print("Haslo prawidłowe")
    else:
        print("Złe hasło, spróbuj jeszcze raz...")
input("Naciśnij ENTER")

print("pętla WHILE wersja 2")
while True:
    haslo = input("Podaj hasło: ")
    if haslo=="ABC":
        print("Haslo prawidłowe")
        break #polecenie break przerywa pętle
    else:
        print("Złe hasło, spróbuj jeszcze raz...")
input ("Naciśnij ENTER")
