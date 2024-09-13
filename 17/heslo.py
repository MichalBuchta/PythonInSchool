passwords = {
    "Jiří": "tajne-heslo",
    "Natálie": "jeste-tajnejsi-heslo",
    "Klára": "nejtajnejsi-heslo"
}

user = input("Zadejte jméno")
if user in passwords:
    heslo = input("Jste na seznamu, nyní zadejte heslo: ")
    if heslo in passwords.get(user):
        print("Smíš vstoupit")
    else:
        print("Špatné heslo")
else:
    print("Nejste na seznamu")