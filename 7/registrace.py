username = input("zadej username: ")
password = input("zadej password: ")
password2 = input("zadej password znovu: ")
email = input("Zadej email: ")

if "@" and "." in (email) and len(email) >= 5:
    if (password) == (password2) and len(password) >= 8:
        print("registrace uspesna")
    else:
        print("chybne zadane heslo nebo mene nez 8 znaku")
else:
    print("Spatny format emailu")