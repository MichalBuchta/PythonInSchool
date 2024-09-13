def bmi(vyska, vaha):
    return(vaha/(vyska*vyska))
    rozsah = "16,5"
    rozsah2 = "18,5"
    rozsah3 = "25"
    rozsah4 = "30"
    rozsah5 = "35"
    rozsah6 = "40"
    if bmi <= rozsah:
        print("Težká podvýživa")
    elif bmi >= rozsah and bmi <= rozsah2:
        print("podváha")
    elif bmi >= rozsah2 and bmi <= rozsah3:
        print("ideální váha")
    elif bmi >= rozsah3 and bmi <= rozsah4:
        print("nadváha")
    elif bmi >= rozsah4 and bmi <= rozsah5:
        print("mírná obezita")
    elif bmi >= rozsah5 and bmi <= rozsah6:
        print("střední obezita")
    elif bmi > rozsah6:
        print("morbidní obezita")
    else:
        print("Chybně zadaná hodnota")
print(bmi(1.72, 72))

