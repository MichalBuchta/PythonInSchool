import random

body = 0
krupier = 0

while True:
    number = random.randint(2, 10)
    krupiercislo = random.randint(2, 10)
    print(number, "toto je tvoje cislo chces pokracovat ?")
    body = body + number
    print(krupiercislo, "toto je cislo krupiera")
    krupier = krupier + krupiercislo
    print("Celkove mas bodu", body)
    print("Krupier ma celkove bodu", krupier)
    a = input("Chces pokracovat?, Y/N")
    if a == "Y":
        number = random.randint(2, 10)
        krupiercislo = random.randint(2, 10)
        print(number, "toto je tvoje cislo chces pokracovat ?")
        body = body + number
        print(krupiercislo, "toto je cislo krupiera")
        krupier = krupier + krupiercislo
        print("Celkove mas bodu", body)
        print("Krupier ma celkove bodu", krupier)
        b = input("Chces pokracovat?, Y/N")
        if b == "Y":
            number = random.randint(2, 10)
            krupiercislo = random.randint(2, 10)
            print(number, "toto je tvoje cislo chces pokracovat ?")
            body = body + number
            print(krupiercislo, "toto je cislo krupiera")
            krupier = krupier + krupiercislo
            print("Celkove mas bodu", body)
            print("Krupier ma celkove bodu", krupier)
            if body > 21:
                print("Prohral si! Mas vic jak 21 bodu.")
                break
        else:
            if body > 21:
                print("Prohral si! Mas vic jak 21 bodu.")
                break
            else:
                print("Skoncil jsi s", body)
                break
    else:
        if body > 21:
            print("Prohral si! Mas vic jak 21 bodu.")
            break
        else:
            print("Skoncil jsi s ", body)
            break
