seznam = [1,2,3,4,5]

def maximum_seznam(seznam):
    nejvetsi = seznam[0]
    for cislo in seznam:
        if cislo > nejvetsi:
            nejvetsi = cislo
    print(nejvetsi)
maximum_seznam(seznam)