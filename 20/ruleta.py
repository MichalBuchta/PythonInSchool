import random

rada1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31]
rada2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32]
rada3 = [3, 6, 9, 12, 15, 16, 21, 24, 27, 30, 33]

def roullete():

    x = random.randint(0,33)

    z = input("Zadej radu od 1 do 3: \n")

    if x == 0:
        if z == "1":
            print("vybral jsi si řadu 1")
            print("Hazim kulicku padlo: ",x)
            print("prohral jsi")
        elif z == "2":
            print("vybral jsi si řadu 2")
            print("Hazim kulicku padlo: ",x)
            print("prohral jsi")
        elif z == "3":
            print("vybral jsi si řadu 3")
            print("Hazim kulicku padlo: ",x)
            print("prohral jsi")
        else:
            print("spatne cislo")
    else:
        if z == "1":
            print("vybral jsi si řadu 1")
            print("Hazim kulicku padlo: ",x)
            if x in rada1:
                print("vyhral jsi")
            else:
                print("prohral jsi")
        elif z == "2":
            print("vybral jsi si řadu 2")
            print("Hazim kulicku padlo: ",x)
            if x in rada2:
                print("vyhral jsi")
            else:
                print("prohral jsi")
        elif z == "3":
            print("vybral jsi si řadu 3")
            print("Hazim kulicku padlo: ",x)
            if x in rada3:
                print("vyhral jsi")
            else:
                print("prohral jsi")
        else:
            print("spatne cislo")
roullete()