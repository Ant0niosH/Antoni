#Antoni Handschuh

print("Podawanie oceny z testu")
print
wynik = int(input("Podaj wynik testu (liczba całkowita)"))
if (wynik < 0) or (wynik > 100):
    print("Podałeś zły wynik")
elif wynik==100:
    print("ocena: CELUJĄCY")
elif wynik>=90:
    print("ocena: BARDZO DOBRY")
elif wynik>=70:
    print("ocena: DOBRY")
elif wynik>=50:
    print("ocena: DOSTATECZNY")
elif wynik>=30:
    print("ocena: DOPUSZCZAJĄCY")
else:
    prin("ocena: NIEDOSTATECZNY")
input("Wciśnij eneter")
