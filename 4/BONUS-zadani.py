kurz = 24.55
listek = 330
navstevniku = 174
predstaveni = 15
navstud = navstevniku/2
pocetstudentu = navstud

mesicniprijem = round(predstaveni*listek*navstevniku)
cena = round(listek/kurz)
cena2 = round(listek/kurz, 2)
studenti = listek*100/65
mesicniprijemsestudenty = round(navstud*studenti+navstud*listek)

print("Divadlo na vstupném vydělá přibližně: ",mesicniprijem,"Kč\n")
print("Cena lístků v eurech: ",cena,"€\n")
print("Cena lístků v eurech a centech: ",cena2,"€\n")
print("Po zavedení studentskách slev měsíční příjem je: ",mesicniprijemsestudenty,"Kč")