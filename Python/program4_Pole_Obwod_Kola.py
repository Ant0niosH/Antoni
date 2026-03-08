#Antoni Handschuh
# Pole i obwód koła

import math

print ("Liczenie Pola i obwodu koła")
promien = int(input("Podaj promień koła: "))
if promien > 0:
    print("Pole koła wynosi = %.6f" % (math.pi * (promien**2)))
    print("Obwód koła wynosi = %.6f" % (math.pi * promien * 2))
    input("Wduś enter aby kontynuować")
elif promien == 0:
    print("Podałeś promień 0, dyskusyjna sprawa. Wybrałeś punkt.")
else:
    print("Podałeś niewłaściwą liczbę.")
    input("Wduś enter aby kontynuować")
