KB3 = []

def pridani_spoluzaka(jmeno, prijmeni):
    KB3.append([prijmeni, jmeno])
pridani_spoluzaka('Jakub', 'Barta')
pridani_spoluzaka('Filip', 'Dohnal')
pridani_spoluzaka('Eduard', 'Buchnicek')

def vypis_spoluzaka(cislo_KL):
    KB3.sort()
    print(KB3[cislo_KL-1])
vypis_spoluzaka(2)