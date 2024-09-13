hesla = [ "heslo123", "puntik", "gilette-fusion", "78910", "20112021", "tereza13", "NaCoHeslo", "simsalabim", "JanAmos", "beruška", "@hojk1"]

for kokot in hesla:
    print(kokot)

print("------------")

for kokot in hesla:
    if kokot > '8':
        print(kokot)

print("-------------")

def pica():
    for kokot in hesla:
        if "-" in kokot:
            print(kokot)
pica()
