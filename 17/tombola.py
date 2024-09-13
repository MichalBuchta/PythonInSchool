TOMBOLA = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balonem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Dostihy a sázky"
}
x = 1
while x != 0:
    user = int(input("Zadejte číslo lístku: "))
    x = len(TOMBOLA.keys())
    if user in TOMBOLA.keys():
        print("Vyhráváte: ", TOMBOLA[user])
        TOMBOLA.pop(user)
        x = x - 1
    else:
        print("Nevyhráváte")
        break