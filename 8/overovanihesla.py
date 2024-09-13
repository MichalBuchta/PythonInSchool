"""username = input("zadej username: ")
password = input("zadej password: ")
password2 = input("zadej password znovu: ")
email = input("Zadej email: ")
password3 = [password]
print(password3)
eu = password3[1]
eu2 = password3[4]
eu3 = password3[6]

cz = password[1]
cz2 = password[4]
cz3 = password[6]
print(eu)

if "@" and "." in (email) and len(email) >= 5:
    if (password) == (password2) and len(password) >= 8:
        print("registrace uspesna")
        print("Zadejte 2, 5, 7 znak vaseho hesla pro overeni identity")
        if (eu and eu2 and eu3) == (cz and cz2 and cz3):
            print("uspesne prihlaseni")
        else:
            print("Overeni identity selhalo")
    else:
        print("chybne zadane heslo nebo mene nez 8 znaku")

else:
    print("Spatny format emailu")"""

heslo = "123456789"
spravny = ""

print("Zadejte 2, 5, 7 znak hesla")
heslo = input(": ")
snfed = heslo[1] + heslo[4] + heslo[6]
if 
