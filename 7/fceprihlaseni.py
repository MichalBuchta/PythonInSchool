def prihlaseni():
    username = input("username: ")
    password = input("zadej password: ")


    if (password) == "NaCoHeslo":
        print("uspesne prihlasen")
    else:
        print("spatne zadany udaje chcete znovu zadat ? Y/N")
        yn = input(": ")
        if (yn) == "Y":
            prihlaseni()
        else:
            exit()
prihlaseni()        
