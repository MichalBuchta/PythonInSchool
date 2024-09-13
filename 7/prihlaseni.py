username = input("zadej username: ")
password = input("zadej password: ")

if (password) == "NaCoHeslo":
    vek = input("zadej věk: ")
    if (vek) >= "18":
        print("uspesne prihlasen")
    else:
        exit()
else:
    print("spatne zadany udaje")
