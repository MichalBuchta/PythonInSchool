heslo = str(input("zadej heslo: "))
list = ["@","!","."]
z = len(heslo)
print(z)

if z < 12:
    print("Malo znaku min 12")
else:
    if list not in (heslo):
        print("chyby specialni charaktery")
    else:
        if heslo.islower():
            if heslo.isupper():
                print("Bezpecne heslo", heslo)
            else:
                print("Chybi velke pismeno")
        else:
            print("chybi male pismeno")
##nefunguje