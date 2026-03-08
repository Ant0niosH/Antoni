#Antoni Handschuh
#Czy podany trójkąt istnieje

bokA = int(input("Podaj bok a: "))
bokB = int(input("Podaj bok b: "))
bokC = int(input("Podaj bok c: "))
obwod = bokA + bokB + bokC
polobwod = (bokA + bokB + bokC)/2
pole = (polobwod*(polobwod-bokA)*(polobwod-bokB)*(polobwod-bokC)) **(1/2)
if(bokA <= 0):
    print("Podaleś błędne wymiary boków.")
elif(bokB <= 0):
    print("Podaleś błędne wymiary boków.")
elif(bokC <= 0):
    print("Podaleś błędne wymiary boków.")    
else:
    if(bokA + bokB < bokC):
        print ("Trójkąt o podanych wymiarach nie istnieje.")
    elif(bokB + bokC < bokA):
        print ("Trójkąt o podanych wymiarach nie istnieje.")
    elif(bokA + bokC < bokB):
        print ("Trójkąt o podanych wymiarach nie istnieje.")
    else:
        if(bokA == bokB == bokC):
            print("Trójkąt jest równoboczny")
            if(bokA**2 + bokB**2 == bokC**2):
                print("Trójkąt prostokątny")
                print("Obwód wynosi=", obwod)
                print("Pole wynosi=", pole)
            elif(bokA**2 + bokB**2 < bokC**2):
                print("Trójkąt ostrokątny")
                print("Obwód wynosi=", obwod)
                print("Pole wynosi=", pole)
            else:
                print("Trójkąt rozwartokątny")
                print("Obwód wynosi= ", obwod)
                print("Pole wynosi= ", pole)
        elif(bokC== bokA):
            print("Trójkąt  jest równoramienny")
            if(bokA**2 + bokB**2 == bokC**2):
                print("Trójkąt prostokątny")
                print("Obwód wynosi= ", obwod)
                print("Pole wynosi= ", pole)
            elif(bokA**2 + bokB**2 < bokC**2):
                print("Trójkąt ostrokątny")
                print("Obwód wynosi= ", obwod)
                print("Pole wynosi= ", pole)
            else:
                print("Trójkąt rozwartokątny")
                print("Obwód wynosi= ", obwod)
                print("Pole wynosi= ", pole)
        elif(bokB== bokA):
            print("Trójkąt  jest równoramienny")
            if(bokA**2 + bokB**2 == bokC**2):
                print("Trójkąt prostokątny")
                print("Obwód wynosi= ", obwod)
                print("Pole wynosi= ", pole)
            elif(bokA**2 + bokB**2 < bokC**2):
                print("Trójkąt ostrokątny")
                print("Obwód wynosi= ", obwod)
                print("Pole wynosi= ", pole)
            else:
                print("Trójkąt rozwartokątny")
                print("Obwód wynosi= ", obwod)
                print("Pole wynosi= ", pole)
        elif(bokC== bokB):
            print("Trójkąt  jest równoramienny")
            if(bokA**2 + bokB**2 == bokC**2):
                print("Trójkąt prostokątny")
                print("Obwód wynosi= ", obwod)
                print("Pole wynosi= ", pole)
            elif(bokA**2 + bokB**2 < bokC**2):
                print("Trójkąt ostrokątny")
                print("Obwód wynosi= ", obwod)
                print("Pole wynosi= ", pole)
            else:
                print("Trójkąt rozwartokątny")
                print("Obwód wynosi= ", obwod)
                print("Pole wynosi= ", pole)
        else:
            print("Trójkąt jest różnoboczny")
            if(bokA**2 + bokB**2 == bokC**2):
                print("Trójkąt prostokątny")
                print("Obwód wynosi= ", obwod)
                print("Pole wynosi= ", pole)
            elif(bokA**2 + bokB**2 < bokC**2):
                print("Trójkąt ostrokątny")
                print("Obwód wynosi= ", obwod)
                print("Pole wynosi= ", pole)
            else:
                print("Trójkąt rozwartokątny")
                print("Obwód wynosi= ", obwod)
                print("Pole wynosi= ", pole)
