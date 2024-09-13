hry = [
  ["Akt", 180],
  ["Vyšetřování ztráty třídní knihy", 95],
  ["Hospoda Na Mýtince", 128],
  ["Vražda v salónním coupé", 144],
  ["Němý Bobeš aneb Český Tarzan", 135],
  ["Cimrman v říši hudby", 100],
  ["Dlouhý, Široký a Krátkozraký", 165],
  ["Posel z Liptákova", 140],
  ["Lijavec", 130],
  ["Dobytí Severního pólu", 111],
  ["Blaník", 187],
  ["Záskok", 210],
  ["Vlasta", 265],
]


for pica in hry:
    print(pica[0])

print("-----------------")

for debil in hry:
    if debil[1] >= 120:
        print(debil[0])

print("-----------------")

for treti in hry:
    hodiny = treti[1] // 60 ##neda zbytek
    minuty = treti[1] % 60
    print(f"Název: {treti[0]}, délka trvání: {hodiny}hod. {minuty}min")



