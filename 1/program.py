delsi = int(input("zadej a: "))
kratsi = int(input("zadej b: "))
metr = 140


obsah = delsi*kratsi
obvod = 2*(delsi+kratsi)
obsah2 = obsah/10000

cena = obsah2 * metr

print("Obsah:",obsah,"cm\nObvod:",obvod,"cm\ncena: ",cena,"kc")