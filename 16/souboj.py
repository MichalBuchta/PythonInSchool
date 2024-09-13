import random
princezna_hp = 100
dragon_hp = 100
while princezna_hp > 0 and dragon_hp > 0:
    princezna_damage = random.randint(0, 30)
    if random.random() > 0.5:
        dragon_hp -= princezna_damage
        print("Princezna zasáhla draka a ubrala mu {} HP".format(princezna_damage))
    else:
        print("Princezna minula!")
    dragon_damage = random.randint(10, 20)
    princezna_hp -= dragon_damage
    print("Drak zasáhl princeznu a ubral jí {} HP".format(dragon_damage))
    print("Princezna HP: {}, Drak HP: {}".format(princezna_hp, dragon_hp))
    if princezna_hp > dragon_hp:
        print("Princezna vede!")
    elif dragon_hp > princezna_hp:
        print("Drak vede!")
    else:
        print("Je to remíza!")
if princezna_hp <= 0:
    print("Princezna prohrála!")
else:
    print("Princezna vyhrála!")